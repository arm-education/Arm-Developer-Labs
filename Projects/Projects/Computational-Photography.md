---
title: "Develop a Novel Computational Photography Pipeline"
description: "This project creates and implements a novel computational photography pipeline that is optimized for Arm-based mobile devices using SME2 and neural technology. This project comes with the possibility of a hardware donation to support your efforts"
subjects:
    - "ML"
    - "Mobile, Graphics, and Gaming"
    - "Edge AI"
requires-team:
    - "No"
platform:
    - "Laptops and Desktops"
    - "AI"
sw-hw:
    - "Software"
support-level: 
    - "Self-Service"
    - "Arm Ambassador Support"
    - "Direct Support from Arm"
publication-date: 2026-01-07
license:
status:
    - "Published" 
donation:

---

![super-resolution](./images/Super-resolution_example_closeup.png)

### Description

**Why this is important?** 

For many consumers, the camera and its associated features are among the most important factors when choosing a new smartphone. Modern capabilities such as night-mode photography and extreme digital zoom increasingly rely on neural networks to enhance image quality, for example by improving the signal-to-noise ratio (SNR). A notable example is the Google Pixel 10 Pro’ [pro-res zoom](https://blog.google/products/pixel/google-pixel-pro-res-zoom/) which uses on-device diffusion models and generative AI to reconstruct fine detail when zooming beyond the optical range. 

With the introduction of Arm’s Scalable Matrix Extension (SME2) in commercial handsets, these advanced neural networks can now run efficiently on the CPU itself. This enables a wider range of devices to incorporate neural networks directly into their photography pipelines, while also promoting more portable software designs that are not tightly coupled to a specific Neural Processing Unit (NPU).


**Project Summary**

This challenge focuses on designing and implementing a novel computational photography pipeline on an Arm-based device. Your solution must implement one of the following example pipelines, or a closely related variant:

	•	Night-mode imaging: Improve the signal-to-noise ratio (SNR) of photographs captured in low-light conditions.
	•	Portrait-mode imaging: Apply realistic bokeh blur effects to background regions in portrait photographs.
	•	Neural ray denoising: Use neural networks to denoise ray-based or rendering-related image data.
	•	Generative AI–based pipelines: Leverage GenAI models, such as style-transfer or diffusion-based approaches, to enhance or transform images.

For example, your approach could involve fine-tuning an existing model, implementing a novel pipeline. The objective is to optimize your pipeline for both inference latency and perceived image quality and the technical criteria, of your project, on which you will be judged, are as follows:

- Must use a quantized neural network, preferably less that 16-bits (i.e. quantized to less the FP16)
- Preferably use the Executorch runtime, designed for running neural networks with the [Arm Neural Technology](https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/arm-neural-technology-in-executorch-1-0) with the [ML Extensions for Vulkan](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample/) backend
- Algorithms should run on an Arm-based CPU with single-instruction multiple data (SIMD) such as [SVE](https://developer.arm.com/Architectures/Scalable%20Vector%20Extensions) or [SME](https://www.arm.com/technologies/sme2) or an [Neural-Graphics](https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics) enabled GPU (either simulation or physical handset once available)

## Prerequisites

- Experience with traditional image processing algorithms (e.g., convolution, filters).
- Intermediate experience or willingness to learn about machine learning for graphics and photography (e.g., neural ray denoising).
- Familiarity with build systems and associated tools such as CMake, docker.
- Experience with object-orientated programming and scripting with langauges such as C++ and Python.
- Some experience or willingness to learn about low-level programming and using APIs such as Vulkan.

## Resources from Arm and our partners

- Blog: [Neural Camera Denoising with Arm SME2](https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/unlocking-the-power-of-neural-camera-denoising-with-arm-sme2)
- Software: [Reference AI Camera Pipelines](https://gitlab.arm.com/kleidi/kleidi-examples/ai-camera-pipelines)
- Blog: [Neural Graphics](https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics)
- Software: [Arm KleidiCV](https://gitlab.arm.com/kleidi/kleidicv)
- Software: [Vkdt open source photography workflow](https://github.com/hanatos/vkdt)
- Blog: [SME2 enabled devices](https://newsroom.arm.com/blog/arm-c1-cpu-cluster-on-device-ai-performance)
- Blog: [Arm Neural Technolog in Executorch 1.0](https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/arm-neural-technology-in-executorch-1-0)
- Tutorial: [Demonstation using Arm VGF backend](https://github.com/pytorch/executorch/blob/main/examples/arm/vgf_minimal_example.ipynb)

## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register). Additionally, if you would like to engage with this project and need assistance with access to hardware, please email  us at Arm-Developer-Labs@arm.com. 

## Benefits 

Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.

To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.

## Attributions

By User:Omegatron - Created by User:Omegatron using the GIMP, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=1836856




