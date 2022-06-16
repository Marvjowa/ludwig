from typing import Optional

from marshmallow_dataclass import dataclass

from ludwig.schema import utils as schema_utils
from ludwig.schema.features import base
from ludwig.schema.features.preprocessing import H3PreprocessingConfig


@dataclass
class H3InputFeatureConfig(schema_utils.BaseMarshmallowConfig, base.BaseFeatureConfig):
    """
    H3InputFeatureConfig is a dataclass that configures the parameters used for an h3 input feature.
    """

    preprocessing: Optional[str] = H3PreprocessingConfig(
    )

    encoder: Optional[str] = schema_utils.StringOptions(
        ["embed", "weighted_sum", "rnn"],
        default="embed",
        description="Encoder to use for this h3 feature.",
    )

    # TODO(#1673): Need some more logic here for validating against input features
    tied: Optional[str] = schema_utils.String(
        default=None,
        allow_none=True,
        description="Name of input feature to tie the weights of the encoder with.  It needs to be the name of a "
                    "feature of the same type and with the same encoder parameters.",
    )
