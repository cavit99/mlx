# Copyright © 2023 Apple Inc.

from mlx.nn.layers.activations import (
    CELU,
    ELU,
    GELU,
    GLU,
    SELU,
    HardShrink,
    Hardswish,
    HardTanh,
    LeakyReLU,
    LogSigmoid,
    LogSoftmax,
    Mish,
    PReLU,
    ReLU,
    ReLU6,
    Sigmoid,
    SiLU,
    Softmax,
    Softmin,
    Softplus,
    Softshrink,
    Softsign,
    Step,
    Tanh,
    celu,
    elu,
    gelu,
    gelu_approx,
    gelu_fast_approx,
    glu,
    hard_shrink,
    hard_tanh,
    hardswish,
    leaky_relu,
    log_sigmoid,
    log_softmax,
    mish,
    prelu,
    relu,
    relu6,
    selu,
    sigmoid,
    silu,
    softmax,
    softmin,
    softplus,
    softshrink,
    softsign,
    step,
    tanh,
)
from mlx.nn.layers.base import Module
from mlx.nn.layers.containers import Sequential
from mlx.nn.layers.convolution import Conv1d, Conv2d, Conv3d
from mlx.nn.layers.convolution_transpose import (
    ConvTranspose1d,
    ConvTranspose2d,
    ConvTranspose3d,
)
from mlx.nn.layers.dropout import Dropout, Dropout2d, Dropout3d
from mlx.nn.layers.embedding import Embedding
from mlx.nn.layers.linear import Bilinear, Identity, Linear
from mlx.nn.layers.normalization import (
    BatchNorm,
    GroupNorm,
    InstanceNorm,
    LayerNorm,
    RMSNorm,
)
from mlx.nn.layers.pooling import (
    AvgPool1d,
    AvgPool2d,
    AvgPool3d,
    MaxPool1d,
    MaxPool2d,
    MaxPool3d,
)
from mlx.nn.layers.positional_encoding import ALiBi, RoPE, SinusoidalPositionalEncoding
from mlx.nn.layers.quantized import QuantizedEmbedding, QuantizedLinear, quantize
from mlx.nn.layers.recurrent import GRU, LSTM, RNN
from mlx.nn.layers.transformer import (
    MultiHeadAttention,
    Transformer,
    TransformerDecoder,
    TransformerDecoderLayer,
    TransformerEncoder,
    TransformerEncoderLayer,
)
from mlx.nn.layers.upsample import Upsample


# Lazy import for weight_norm to avoid circular import
def _load_weight_norm():
    from mlx.nn.layers.weight_norm import (
        WeightNormConv1d,
        WeightNormConv2d,
        WeightNormLinear,
        weight_norm,
    )

    return WeightNormConv1d, WeightNormConv2d, WeightNormLinear, weight_norm


# Execute after all other imports
WeightNormConv1d, WeightNormConv2d, WeightNormLinear, weight_norm = _load_weight_norm()
