"""Products service for product-related API endpoints."""
from itertools import product
from typing import Optional

from .base import BaseService
from ..models import ProductDetailResponse, ProductSearchResponse


class ProductsService(BaseService):
    """
    Service for product-related API operations.

    Example:
        ```python
        async with DigikalaClient(api_key="...") as client:
            # Get product details
            product = await client.products.get_product(id=12345)
            print(product.data.product.title_fa)

            # Search products
            search_results = await client.products.search(q="iphone", page=1)
            for product in search_results.data.products:
                print(product.title_fa)
        ```
    """

    async def get_product(self, id: int) -> ProductDetailResponse:
        """
        Get detailed product information by ID.

        Args:
            id: Product ID

        Returns:
            ProductDetailResponse containing full product details

        Raises:
            NotFoundError: If product with given ID does not exist
            DigikalaAPIError: For other API errors

        Example:
            ```python
            product = await client.products.get_product(id=12345)
            print(f"Title: {product.data.product.title_fa}")
            print(f"Price: {product.data.product.default_variant.price.selling_price}")
            print(f"Brand: {product.data.product.brand.title_fa}")
            ```
        """
        endpoint = f"/fresh/v1/product/{id}/"
        #TOOD: Check ProductDetailResponse for fresh product details
        return await self._request(
            method="GET",
            endpoint=endpoint,
            response_model=ProductDetailResponse
        )
