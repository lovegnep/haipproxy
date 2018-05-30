"""
We use this validator to filter ip that can access mobile zhihu website.
"""
from config.settings import (
    TEMP_WCGROUP_QUEUE, VALIDATED_WCGROUP_QUEUE,
    TTL_WCGROUP_QUEUE, SPEED_WCGROUP_QUEUE)
from ..redis_spiders import ValidatorRedisSpider
from .base import BaseValidator


class WcGroupValidator(BaseValidator, ValidatorRedisSpider):
    """This validator checks the liveness of wcgroup proxy resources"""
    name = 'wcgroup'
    urls = [
        'https://www.weixinqun.com/index'
    ]
    task_queue = TEMP_WCGROUP_QUEUE
    score_queue = VALIDATED_WCGROUP_QUEUE
    ttl_queue = TTL_WCGROUP_QUEUE
    speed_queue = SPEED_WCGROUP_QUEUE
    success_key = '爬虫'
