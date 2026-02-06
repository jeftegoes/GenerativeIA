# Generative AI <!-- omit in toc -->

## Contents <!-- omit in toc -->

- [1. Overview](#1-overview)
  - [1.1. GenAI - Generative AI](#11-genai---generative-ai)
  - [1.2. NLP - Natural Language Processing](#12-nlp---natural-language-processing)
  - [1.3. LLMs - Large Language Models](#13-llms---large-language-models)
  - [1.4. CV - Computer Vision](#14-cv---computer-vision)
  - [1.5. DL - Deep Learning](#15-dl---deep-learning)
  - [1.6. RL - Reinforcement Learning](#16-rl---reinforcement-learning)
  - [1.7. RPA - Robotic Process Automation](#17-rpa---robotic-process-automation)
  - [1.8. ML - Machine Learning](#18-ml---machine-learning)
- [2. Biological Fundamentals of Human Neural Networks](#2-biological-fundamentals-of-human-neural-networks)
  - [2.1. Introduction](#21-introduction)
  - [2.2. Human Neural Networks](#22-human-neural-networks)
  - [2.3. What Is a Neural Network?](#23-what-is-a-neural-network)
  - [2.4. Structure of a Neuron](#24-structure-of-a-neuron)
  - [2.5. Synapse and Information Processing](#25-synapse-and-information-processing)
- [3. Artificial Neuron: The Perceptron](#3-artificial-neuron-the-perceptron)
  - [3.1. Introduction](#31-introduction)
  - [3.2. From Biological to Artificial Neurons](#32-from-biological-to-artificial-neurons)
  - [3.3. Structure of an Artificial Neuron](#33-structure-of-an-artificial-neuron)
  - [3.4. Example: Sum and Step Functions](#34-example-sum-and-step-functions)
  - [3.5. Learning with the AND Logical Operator](#35-learning-with-the-and-logical-operator)
  - [3.6. Training the Perceptron](#36-training-the-perceptron)
  - [3.7. Knowledge Representation](#37-knowledge-representation)
  - [3.8. Single-Layer Perceptron](#38-single-layer-perceptron)
  - [3.9. Linear Separability](#39-linear-separability)
  - [3.10. Limitation of Single-Layer Perceptrons](#310-limitation-of-single-layer-perceptrons)
  - [3.11. Conclusion](#311-conclusion)

# 1. Overview

## 1.1. GenAI - Generative AI

[GenAI](GenAI.md)

## 1.2. NLP - Natural Language Processing

[NLP](NLP.md)

## 1.3. LLMs - Large Language Models

[LLMs](LLMs.md)

## 1.4. CV - Computer Vision

[CV](CV.md)

## 1.5. DL - Deep Learning

[DL](DL.md)

## 1.6. RL - Reinforcement Learning

[RL](RL.md)

## 1.7. RPA - Robotic Process Automation

[RPA](RPA.md)

## 1.8. ML - Machine Learning

[ML](ML.md)

# 2. Biological Fundamentals of Human Neural Networks

## 2.1. Introduction

- This presents the basic biological concepts of human neural networks, which are essential for understanding artificial neural networks.
- Artificial neural networks are inspired by how the human brain works.

## 2.2. Human Neural Networks

- The human brain contains **more than 100 billion neurons**.
- Neurons are highly **interconnected**, forming a complex network.
- **Information flows** from one neuron to another through these connections.
- This flow of information enables human abilities such as walking, seeing, speaking, thinking, and learning.
  - Learning new skills, such as a new language, leads to the creation of **new neural connections** in the brain.
    ![Human Neural Networks](/Images/HumanNeuralNetworks.jpg)

## 2.3. What Is a Neural Network?

- A neural network is a set of interconnected neurons that exchange information.

## 2.4. Structure of a Neuron

- A neuron has four main components:
  1. **Dendrites** – receive data from other neurons.
  2. **Cell body** – processes the received data.
  3. **Axon** – transmits signals to other neurons.
  4. **Axon terminals** – send signals to connected neurons.
- Together, these components allow the neuron to function as an **information processing unit**.
  ![Structure of a Neuron](/Images/StructureNeuron.png)

## 2.5. Synapse and Information Processing

- A **synapse** is the transmission of information between neurons.
- Information is transmitted as **electrical signals**.
- This process starts at the dendrites and ends at the axon terminals.
- During a synapse, **chemical substances** are released and affect the electrical potential of the receiving neuron.
  - The electrical potential determines how information is processed and leads to decision-making in the brain.

# 3. Artificial Neuron: The Perceptron

## 3.1. Introduction

- How an artificial neuron, called a **perceptron**, works?
  - It builds on the biological fundamentals of neural networks, especially how neurons process and transmit information.

## 3.2. From Biological to Artificial Neurons

- Biological neurons transmit **electrical signals**.
- Artificial neurons transmit **data**.
- Inputs represent information from the environment.
- Outputs represent the final response, such as a prediction.

## 3.3. Structure of an Artificial Neuron

- An artificial neuron consists of:
  - **Inputs** (data from the environment)
  - **Weights** (importance of each input)
  - **Sum function**
  - **Activation function** (step function)
  - **Output**
- Each input is multiplied by its corresponding weight, and the results are summed.

## 3.4. Example: Sum and Step Functions

1. Inputs are multiplied by weights.
2. The results are added using the **sum function**.
3. The **step function** is applied:
   - If the sum ≥ 1, output = 1
   - Otherwise, output = 0

- This process defines the perceptron’s prediction.
  ![Artificial Neuron -> Perceptron = 1](/Images/ArtificialNeuron_1.png)
  ![Artificial Neuron -> Perceptron = 0](/Images/ArtificialNeuron_2.png)

## 3.5. Learning with the AND Logical Operator

The perceptron is trained to learn the **AND** logical operator:

- Inputs: x¹ and x²
- Output (class): true (1) or false (0)
- **Truth table**
  ![alt](/Images/TruthTable.png)

## 3.6. Training the Perceptron

1. Apply the sum and activation functions to each row.
2. Compare the predicted output with the expected output.
3. Calculate the **error**.
4. Update the weights using the formula:
   - new weight = current weight + (learning rate × input × error)
   - The **learning rate** controls how fast the weights are adjusted.
   - Training continues until the error becomes zero.

## 3.7. Knowledge Representation

- The **knowledge of a neural network is stored in its weights**.
- Training adjusts weights until the network correctly classifies all inputs.

## 3.8. Single-Layer Perceptron

![alt](/Images/SingleLayerPerceptron.png)

## 3.9. Linear Separability

- **AND** and **OR** operators are **linearly separable** (can be separated by a straight line).
- **XOR** is **not linearly separable**, meaning a single straight line cannot separate its classes.

## 3.10. Limitation of Single-Layer Perceptrons

- **Single-layer perceptrons** work well for simple problems.
- They cannot solve complex or non-linearly separable problems.
- More complex architectures are required.

## 3.11. Conclusion

- To solve real-world problems, neural networks need more advanced structures.
