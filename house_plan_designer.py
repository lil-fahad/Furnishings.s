
import torch
from PIL import Image
import numpy as np
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel, UniPCMultistepScheduler

class PretrainedHousePlanDesigner:
    def __init__(self, device="cuda"):
        controlnet = ControlNetModel.from_pretrained(
            "lllyasviel/sd-controlnet-canny", torch_dtype=torch.float16
        )
        self.pipeline = StableDiffusionControlNetPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            controlnet=controlnet,
            torch_dtype=torch.float16,
        ).to(device)
        self.pipeline.scheduler = UniPCMultistepScheduler.from_config(self.pipeline.scheduler.config)

    def generate(self, plan_image_path: str, prompt: str, num_images: int = 1):
        plan_image = Image.open(plan_image_path).convert("RGB")
        processed_image = np.array(plan_image)
        processed_image = Image.fromarray(processed_image)

        output = self.pipeline(
            prompt,
            image=processed_image,
            num_inference_steps=30,
            guidance_scale=7.5,
            num_images_per_prompt=num_images
        ).images

        for idx, img in enumerate(output):
            img.save(f"generated_design_{idx + 1}.png")

        return output
