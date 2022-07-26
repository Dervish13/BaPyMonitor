try:
    from .local_config import DevConfig
except ImportError:
    from .common_config import DevConfig

try:
    from .local_config import ProdConfig
except ImportError:
    from .common_config import ProdConfig

configs = {
    'development': DevConfig,
    'production': ProdConfig,
    'default': ProdConfig,
}
