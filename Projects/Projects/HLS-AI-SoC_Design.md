---
title: "Specialized AI Accelerator SoC Design using HLS"
description: "Explore using Catapult High-Level Synthesis (HLS) to transform AI models into accelerator hardware that can integrate with Arm IP in a tape-out-capable SoC."
subjects:
  - "ML"
  - "Performance and Architecture"
requires-team:
  - "No"
platform:
  - "AI"
sw-hw:
  - "Software"
  - "Hardware"
support-level:
  - "Self-Service"
  - "Arm Ambassador Support"
publication-date: 2026-01-16
license:
status:
  - "Hidden"
---

![learn_on_arm](../../images/Learn_on_Arm_banner.png)

# SoC Labs Logo

## Description

### Why is this important?

High-Level Synthesis (HLS) tools such as Catapult allow designers to translate high-level algorithm descriptions into synthesizable RTL, significantly accelerating the development of custom hardware. These tools are increasingly relevant for implementing machine learning workloads in dedicated accelerators. However, there remains a gap between experimental accelerator development and reproducible, tape-out-ready ASIC design flows.

Many AI accelerator projects focus on a single model, dataset, or hardware platform. While useful for demonstrating performance, these efforts often lack a clearly documented methodology that can be reused across different designs and projects.

This project aims to address that gap by defining a structured workflow for translating AI models into hardware IP suitable for integration into an Arm-based SoC and eventual fabrication.

The goal is to establish a clear development path from:

AI model → Catapult HLS (or similar tool) → RTL → Arm-based SoC integration → tape-out

By documenting this process, the project seeks to reduce the cost, complexity, and expertise barrier associated with developing custom AI accelerators for silicon. Such a workflow could support startups, academic groups, and independent developers interested in deploying specialised hardware alongside Arm processors.

### Project Summary

This project investigates the use of Catapult HLS (and similar tools) to create a practical workflow for generating specialised AI accelerator IP derived from machine learning models and integrating it into an Arm-based SoC design.

Unlike a programmable NPU, which is designed to support a wide range of neural networks, this approach focuses on accelerators tailored to specific models or workloads. This makes it particularly suitable for fixed-function inference tasks in embedded systems, edge AI devices, and domain-specific SoCs where efficiency and simplicity are priorities.

Rather than targeting a single accelerator architecture or machine learning model, the project focuses on defining a methodology and reference design flow that can be applied across multiple workloads and design contexts.

The project is structured around three key layers:

AI and software layer
- Selection of representative AI models (e.g. CNNs, transformers, or classical machine learning algorithms).
- Application of model optimisation techniques such as quantisation, pruning, and compression to improve hardware efficiency.
- Mapping between software frameworks (e.g. TensorFlow or PyTorch) and hardware-friendly algorithm representations suitable for HLS implementation.

Hardware generation layer
- Use of Catapult HLS to convert high-level C/C++ algorithm descriptions into synthesizable RTL.
- Identification of constraints and design considerations required for ASIC-ready RTL, including memory architecture, datapath organisation, and interface design.
- Definition of coding guidelines, verification strategies, and interface standards that enable reproducible hardware generation.

SoC Design
- Integration of the generated accelerator as an IP block within an Arm-based SoC architecture.
- Documentation of the additional steps required beyond functional validation, including synthesis, timing closure, verification, and power/area analysis.
- Identification of the practical differences between prototype-level designs and fabrication-ready implementations.

The primary outcome of this project will be a reference design flow, example implementations, and supporting documentation demonstrating how AI models can be systematically translated into accelerator IP suitable for integration into real Arm-based silicon.

## What will you use?
You should be familiar with, or willing to learn about:
- High-level Synthesis (HLS), including Catapult HLS or similar tools
- Machine learning frameworks (e.g. TensorFlow, PyTorch)
- AI model optimisation for hardware (quantisation, pruning)
- RTL and digital design basics
- Arm-based SoC and accelerator integration concepts
- Software–hardware co-design
- Reproducible design workflows

## Resources from Arm and our partners

# TODO

## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

This project can also be supported by SoC Labs in Southampton. 
# TODO

## Benefits 

Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.

To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.

