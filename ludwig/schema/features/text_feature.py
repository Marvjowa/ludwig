from typing import Optional
from ludwig.constants import TEXT

from marshmallow_dataclass import dataclass

from ludwig.encoders.registry import get_encoder_classes
from ludwig.decoders.registry import get_decoder_classes

from ludwig.schema import utils as schema_utils
from ludwig.schema.preprocessing import BasePreprocessingConfig, PreprocessingDataclassField


@dataclass
class TextInputFeatureConfig(schema_utils.BaseMarshmallowConfig):
    """
    TextInputFeatureConfig is a dataclass that configures the parameters used for a text input feature.
    """

    preprocessing: BasePreprocessingConfig = PreprocessingDataclassField(
        feature_type=TEXT
    )

    encoder: Optional[str] = schema_utils.StringOptions(
        list(get_encoder_classes(TEXT).keys()),
        default="parallel_cnn",
        description="Encoder to use for this text feature.",
    )


@dataclass
class TextOutputFeatureConfig(schema_utils.BaseMarshmallowConfig):
    """
    TextOutputFeatureConfig is a dataclass that configures the parameters used for a text output feature.
    """

    decoder: Optional[str] = schema_utils.StringOptions(
        list(get_decoder_classes(TEXT).keys()),
        default="generator",
        description="Decoder to use for this text output feature.",
    )
