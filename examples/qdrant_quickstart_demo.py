import asyncio

from qdrant_client import AsyncQdrantClient, models

QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "quickstart_demo"
VECTOR_SIZE = 4


async def main():
    # 直接初始化客户端，方便单独学习 quickstart 的基本用法
    client = AsyncQdrantClient(url=QDRANT_URL)
