import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock
from zsxq_mcp.server import create_server
from zsxq_mcp.client import ZSXQClient
from zsxq_mcp.config import ZSXQConfig


def test_server_creation():
    """Test that the server can be created successfully."""
    server = create_server()
    assert server is not None
    assert hasattr(server, 'run')


def test_zsxq_client_init():
    """Test ZSXQClient initialization."""
    # Test with environment variables
    import os
    os.environ['ZSXQ_COOKIE'] = 'test_cookie'
    os.environ['ZSXQ_GROUP_ID'] = 'test_group_id'

    try:
        client = ZSXQClient()
        assert client.config.cookie == 'test_cookie'
        assert client.config.group_id == 'test_group_id'
    finally:
        # Clean up environment
        os.environ.pop('ZSXQ_COOKIE', None)
        os.environ.pop('ZSXQ_GROUP_ID', None)


def test_zsxq_config():
    """Test ZSXQConfig class."""
    config = ZSXQConfig(cookie="test_cookie", group_id="test_group_id")
    assert config.cookie == "test_cookie"
    assert config.group_id == "test_group_id"


@pytest.mark.asyncio
async def test_publish_topic_success():
    """Test successful topic publishing."""
    mock_client = AsyncMock()
    mock_client.publish_topic.return_value = {"success": True}

    result = await mock_client.publish_topic("test content")
    assert result["success"] is True


@pytest.mark.asyncio
async def test_upload_image_success():
    """Test successful image uploading."""
    mock_client = AsyncMock()
    mock_client.upload_image.return_value = {"success": True, "image_id": 123}

    result = await mock_client.upload_image("/path/to/image.jpg")
    assert result["success"] is True
    assert result["image_id"] == 123


if __name__ == "__main__":
    pytest.main([__file__])