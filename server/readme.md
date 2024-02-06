# Captcha Solving Browser Extension using CNN

## Overview

This browser extension is designed to solve captchas using Convolutional Neural Networks (CNN). It integrates seamlessly with popular web browsers and provides an efficient solution for automating captcha solving tasks.

![Captcha Solving Demo](demo.gif)

## Features

- Captcha solving using CNN
- Browser extension support for [Chrome](https://www.google.com/chrome/) and [Firefox](https://www.mozilla.org/firefox/)
- Easy integration with existing browser setups
- Configurable settings for different captcha types

## Installation

### Chrome

1. Clone the repository or download the ZIP file.
2. Open the Chrome browser.
3. Navigate to `chrome://extensions/`.
4. Enable "Developer mode" in the top right corner.
5. Click on "Load unpacked" and select the extension folder.

### Firefox

1. Clone the repository or download the ZIP file.
2. Open the Firefox browser.
3. Navigate to `about:debugging#/runtime/this-firefox`.
4. Click on "Load Temporary Add-on" and select the `manifest.json` file from the extension folder.

## Usage

1. Open the target website with a captcha challenge.
2. Click on the extension icon in the browser toolbar.
3. The extension will analyze and attempt to solve the captcha automatically.

## Configuration

Customize the extension's behavior by modifying the configuration settings in `config.json`. Adjust parameters such as CNN model weights, threshold values, and captcha type recognition.

```json
{
  "model_weights": "path/to/your/model_weights.h5",
  "threshold": 0.8,
  "captcha_type": "numeric"
}
