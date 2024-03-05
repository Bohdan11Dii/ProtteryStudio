from typing import TypeVar

InstanceImage = TypeVar("InstanceImage", bound="Image")

def product_directory_path(instance: InstanceImage, filename: str) -> str:
    product = instance.product_id.name if instance.product_id else "delete_images"
    return f"image/{product}/{filename}"