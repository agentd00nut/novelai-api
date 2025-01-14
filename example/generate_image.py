"""
{filename}
==============================================================================

| Example of how to generate an image
|
| The resulting images will be placed in a folder named "results"
"""

import asyncio
from pathlib import Path

from example.boilerplate import API
from novelai_api.ImagePreset import ImageModel, ImagePreset, ImageResolution, UCPreset


async def main():
    d = Path("results")
    d.mkdir(exist_ok=True)

    async with API() as api_handler:
        api = api_handler.api

        preset = ImagePreset()
        preset.seed = 42

        # multiple images
        # preset.n_samples = 4
        i = 0
        async for _, img in api.high_level.generate_image("1girl", ImageModel.Anime_Full, preset):
            (d / f"image_1_{i}.png").write_bytes(img)

            i += 1

        # custom size
        preset.n_samples = 1
        preset.resolution = (128, 256)

        async for _, img in api.high_level.generate_image("1girl", ImageModel.Anime_Full, preset):
            (d / "image_2.png").write_bytes(img)

        # furry model
        preset.resolution = ImageResolution.Normal_Square
        # Furry model has no Bad Anatomy UC Preset
        preset.uc_preset = UCPreset.Preset_Low_Quality

        async for _, img in api.high_level.generate_image("female, species:human", ImageModel.Furry, preset):
            (d / "image_3.png").write_bytes(img)


if __name__ == "__main__":
    asyncio.run(main())
