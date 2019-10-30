from keras.models import Model
from keras.layers import Input
from keras.layers.core import Dropout, Lambda
from keras.layers.convolutional import Conv2D, Conv2DTranspose
from keras.layers.pooling import MaxPooling2D
from keras.layers.merge import concatenate


def U_Net(image_shape, activation='elu', numInitChannels=16, fixed_dropout=0.0, 
          spatial_dropout=False):
    """Create the U-Net

       Args:
            image_shape (array of 3 int): dimensions of the input image.
            activation (str, optional): Keras available activation type.
            numInitChannels (int, optional): number of convolution channels to 
            start with. In each downsampling/upsampling the number of filters 
            are multiplied/divided by 2.
            fixed_dropout (float, optional): dropout value to be fixed. If no 
            value is provided the default behaviour will be to select a 
            piramidal value stating from 0.1 and reaching 0.3 value.
            spatial_dropout (bool, optional): use spatial dropout instead of the
            "normal" dropout. 

       Returns:
            model (Keras model): model containing the U-Net created.
    """
    inputs = Input((image_shape[0], image_shape[1], image_shape[2]))
    s = Lambda(lambda x: x / 255) (inputs)
    
    c1 = Conv2D(numInitChannels, (3, 3), activation=activation,
                kernel_initializer='he_normal', padding='same') (s)
    if fixed_dropout == 0.0:
        c1 = Dropout(0.1) (c1)
        #c1 = SpatialDropout2D(0.1) (c1) if dropout_value else Dropout(0.1) (c1)
    else:
        c1 = Dropout(fixed_dropout) (c1)
        #c1 = SpatialDropout2D(fixed_dropout) (c1) if dropout_value else Dropout(fixed_dropout) (c1)

    c1 = Conv2D(numInitChannels, (3, 3), activation=activation,
                kernel_initializer='he_normal', padding='same') (c1)
    p1 = MaxPooling2D((2, 2)) (c1)
    
    c2 = Conv2D(numInitChannels*2, (3, 3), activation=activation,
                kernel_initializer='he_normal', padding='same') (p1)
    if fixed_dropout == 0.0:
        c2 = Dropout(0.1) (c2)
        #c2 = SpatialDropout2D(0.1) (c2) if dropout_value else Dropout(0.1) (c2)
    else:
        c2 = Dropout(fixed_dropout) (c2)
        #c2 = SpatialDropout2D(fixed_dropout) (c2) if dropout_value else Dropout(fixed_dropout) (c2)
    c2 = Conv2D(numInitChannels*2, (3, 3), activation=activation,
                kernel_initializer='he_normal', padding='same') (c2)
    p2 = MaxPooling2D((2, 2)) (c2)
    
    c3 = Conv2D(numInitChannels*4, (3, 3), activation=activation,
                kernel_initializer='he_normal', padding='same') (p2)
    if fixed_dropout == 0.0:
        c3 = Dropout(0.2) (c3)
        #c3 = SpatialDropout2D(0.1) (c3) if dropout_value else Dropout(0.1) (c3)
    else:    
        c3 = Dropout(fixed_dropout) (c3)
        #c3 = SpatialDropout2D(fixed_dropout) (c3) if dropout_value else Dropout(fixed_dropout) (c3)
    c3 = Conv2D(numInitChannels*4, (3, 3), activation=activation,
                kernel_initializer='he_normal', padding='same') (c3)
    p3 = MaxPooling2D((2, 2)) (c3)
    
    c4 = Conv2D(numInitChannels*8, (3, 3), activation=activation,
                kernel_initializer='he_normal', padding='same') (p3)
    if fixed_dropout == 0.0:
        c4 = Dropout(0.2) (c4)
        #c4 = SpatialDropout2D(0.1) (c4) if dropout_value else Dropout(0.1) (c4)
    else:
        c4 = Dropout(fixed_dropout) (c4)
        #c4 = SpatialDropout2D(fixed_dropout) (c4) if dropout_value else Dropout(fixed_dropout) (c4)
    c4 = Conv2D(numInitChannels*8, (3, 3), activation=activation,
                kernel_initializer='he_normal', padding='same') (c4)
    p4 = MaxPooling2D(pool_size=(2, 2)) (c4)
    
    c5 = Conv2D(numInitChannels*16, (3, 3), activation=activation,
                kernel_initializer='he_normal', padding='same') (p4)
    if fixed_dropout == 0.0:
        c5 = Dropout(0.3) (c5)
        #c5 = SpatialDropout2D(0.1) (c5) if dropout_value else Dropout(0.1) (c5)
    else:
        c5 = Dropout(fixed_dropout) (c5)
        #c5 = SpatialDropout2D(fixed_dropout) (c5) if dropout_value else Dropout(fixed_dropout) (c5)
    c5 = Conv2D(numInitChannels*16, (3, 3), activation=activation,
                kernel_initializer='he_normal', padding='same') (c5)
    
    u6 = Conv2DTranspose(numInitChannels*8, (2, 2), strides=(2, 2),
                         padding='same') (c5)
    u6 = concatenate([u6, c4])
    c6 = Conv2D(numInitChannels*8, (3, 3), activation=activation,
                kernel_initializer='he_normal', padding='same') (u6)
    if fixed_dropout == 0.0:
        c6 = Dropout(0.2) (c6)
        #c6 = SpatialDropout2D(0.1) (c6) if dropout_value else Dropout(0.1) (c6)
    else:
        c6 = Dropout(fixed_dropout) (c6)
        #c6 = SpatialDropout2D(fixed_dropout) (c6) if dropout_value else Dropout(fixed_dropout) (c6)
    c6 = Conv2D(numInitChannels*8, (3, 3), activation=activation,
                kernel_initializer='he_normal', padding='same') (c6)
    
    u7 = Conv2DTranspose(numInitChannels*4, (2, 2), strides=(2, 2),
                         padding='same') (c6)
    u7 = concatenate([u7, c3])
    c7 = Conv2D(numInitChannels*4, (3, 3), activation=activation,
                kernel_initializer='he_normal', padding='same') (u7)
    if fixed_dropout == 0.0:
        c7 = Dropout(0.2) (c7)
        #c7 = SpatialDropout2D(0.1) (c7) if dropout_value else Dropout(0.1) (c7)
    else:
        c7 = Dropout(fixed_dropout) (c7)
        #c7 = SpatialDropout2D(fixed_dropout) (c7) if dropout_value else Dropout(fixed_dropout) (c7)
    c7 = Conv2D(numInitChannels*4, (3, 3), activation=activation,
                kernel_initializer='he_normal', padding='same') (c7)
    
    u8 = Conv2DTranspose(numInitChannels*2, (2, 2), strides=(2, 2),
                         padding='same') (c7)
    u8 = concatenate([u8, c2])
    c8 = Conv2D(numInitChannels*2, (3, 3), activation=activation,
                kernel_initializer='he_normal', padding='same') (u8)
    if fixed_dropout == 0.0:
        c8 = Dropout(0.1) (c8)
        #c8 = SpatialDropout2D(0.1) (c8) if dropout_value else Dropout(0.1) (c8)
    else:
        c8 = Dropout(fixed_dropout) (c8)
        #c8 = SpatialDropout2D(fixed_dropout) (c8) if dropout_value else Dropout(fixed_dropout) (c8)
    c8 = Conv2D(numInitChannels*2, (3, 3), activation=activation,
                kernel_initializer='he_normal', padding='same') (c8)
    
    u9 = Conv2DTranspose(numInitChannels, (2, 2), strides=(2, 2),
                         padding='same') (c8)
    u9 = concatenate([u9, c1], axis=3)
    c9 = Conv2D(numInitChannels, (3, 3), activation=activation,
                kernel_initializer='he_normal', padding='same') (u9)
    if fixed_dropout == 0.0:
        c9 = Dropout(0.1) (c9)
        #c9 = SpatialDropout2D(0.1) (c9) if dropout_value else Dropout(0.1) (c9)
    else:
        c9 = Dropout(fixed_dropout) (c9)
        #c9 = SpatialDropout2D(fixed_dropout) (c9) if dropout_value else Dropout(fixed_dropout) (c9)
    c9 = Conv2D(numInitChannels, (3, 3), activation=activation,
                kernel_initializer='he_normal', padding='same') (c9)
    
    outputs = Conv2D(1, (1, 1), activation='sigmoid') (c9)
    
    model = Model(inputs=[inputs], outputs=[outputs])
    
    return model
