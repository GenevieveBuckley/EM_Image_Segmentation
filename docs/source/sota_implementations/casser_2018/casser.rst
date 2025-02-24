Casser et al.
.............

As part of our paper we try to reproduce other state-of-the-art approaches for EM semantic segmentation 
that do not provide code. In this case the following paper has been reproduced:

.. code-block:: bash

    Vincent Casser, Kai Kang, Hanspeter Pfister, and Daniel Haehn, "Fast mitochondria 
    segmentation for connectomics", arXiv preprint arXiv:1812.06024 (2018)

`[Paper] <https://arxiv.org/abs/1812.06024>`_ `[Our code] <https://github.com/danifranco/EM_Image_Segmentation/tree/v1.0/sota_implementations/casser_2018>`_ 

We have prepared two templates:

    - `casser_template_V0.py <https://github.com/danifranco/EM_Image_Segmentation/tree/v1.0/sota_implementations/casser_2018/casser_template_V0.py>`_ : exact parameters and training workflow as described in the paper.
    - `casser_template_V1.py <https://github.com/danifranco/EM_Image_Segmentation/tree/v1.0/sota_implementations/casser_2018/casser_template_V1.py>`_ : changes made respect to V0 with which we have achieved better results.

The implementation is based in one file:
    - `2D U-Net <casser_network.html>`_: proposed 2D U-Net (recently submitted by the authors `here <https://github.com/mpsych/mitochondria>`_).

Here is a picture of the network extracted from the original paper:
                                                                                
.. image:: ../../img/casser_network.png
    :width: 100%                                                         
    :align: center 
