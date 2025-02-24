from tensorflow import keras
from tensorflow.keras import layers

def create_oztel_model(num_classes=2, input_shape=(None, None, 1)):
    """Create the CNN proposed by Oztel et. al.

       Parameters
       ----------   
       num_classes : int, optional
           Number of classes to predict.
        
       input_shape : 3D tuple, optional
           Dimensions of the input image.

       Returns
       -------
       model : Keras model
           Model containing the CNN created.


       Here is a picture of the network extracted from the original paper:
                                                                                
       .. image:: ../../img/oztel_network.png
           :width: 100%                                                         
           :align: center
    """

    model = keras.Sequential(
        [
            # Block 1
            keras.Input(shape=input_shape),
            layers.BatchNormalization(),
            layers.Conv2D(32, kernel_size=(5, 5), padding='same', strides=1),
            layers.MaxPooling2D(pool_size=(3, 3), strides=(2,2), padding='same' ),
            layers.Activation('relu'),
            # Block 2
            layers.Conv2D(32, kernel_size=(5, 5), padding='same', activation="relu"),
            layers.AveragePooling2D(pool_size=(3, 3), strides=2, padding='same'),
            layers.Dropout(0.5),
            # Block 3
            layers.Conv2D(64, kernel_size=(5, 5), padding='same', activation="relu"),
            layers.AveragePooling2D(pool_size=(3, 3), strides=2, padding='same'),
            # Block 4
            layers.Conv2D(64, kernel_size=(4, 4), strides=1, padding='valid', activation="relu"),
            layers.Conv2D(num_classes, (1, 1), activation='softmax'),
        ]
    )

    return model


def create_oztel_model_V1(num_classes=2, input_shape=(None, None, 1)):
    """Create the CNN proposed by Oztel et. al.                                 
                                                                                
       Parameters                                                               
       ----------                                                               
       num_classes : int, optional                                              
           Number of classes to predict.                                        
                                                                                
       input_shape : 3D tuple, optional                                         
           Dimensions of the input image.                                       
                                                                                
       Returns                                                                  
       -------                                                                  
       model : Keras model                                                      
           Model containing the CNN created.                                    
                                                                                
                                                                                
       Here is a picture of the network extracted from the original paper:      
                                                                                
       .. image:: ../../img/oztel_network.png                                         
           :width: 100%                                                         
           :align: center                                                       
    """ 

    model = keras.Sequential(
        [
            # Block 1
            keras.Input(shape=input_shape),
            layers.Conv2D(16, kernel_size=(3, 3), padding='same', strides=1),
            layers.BatchNormalization(),
            layers.Activation( 'relu' ),
            layers.Dropout( 0.1 ),
            layers.Conv2D(16, kernel_size=(3, 3), padding='same', strides=1),
            layers.BatchNormalization(),
            layers.Activation( 'relu' ),
         
            layers.MaxPooling2D((2,2)),

            # Block 2
            layers.Conv2D(32, kernel_size=(3, 3), padding='same', strides=1),
            layers.BatchNormalization(),
            layers.Activation( 'relu' ),
            layers.Dropout( 0.2 ),
            layers.Conv2D(32, kernel_size=(3, 3), padding='same', strides=1),
            layers.BatchNormalization(),
            layers.Activation( 'relu' ),
            
            layers.MaxPooling2D((2,2)),

            # Block 3
            layers.Conv2D(32, kernel_size=(3, 3), padding='same', strides=1),
            layers.BatchNormalization(),
            layers.Activation( 'relu' ),
            layers.Dropout( 0.3 ),
            layers.Conv2D(32, kernel_size=(3, 3), padding='same', strides=1),
            layers.BatchNormalization(),
            layers.Activation( 'relu' ),
         
            layers.MaxPooling2D((2,2)),

            # Block 4
            layers.Conv2D(64, kernel_size=(4, 4), strides=1, padding='valid'),
            layers.BatchNormalization(),
            layers.Activation( 'relu' ),
            layers.Conv2D(num_classes, (1, 1), activation='softmax'),
        ]
    )

    return model
