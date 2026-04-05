

<h3 align="center">EV Charging Prediction Model</h3>

  <p align="center">
    A Machine Learning application to predict Electric Vehicle charging session success and monitor station parameters!
    <br />
    <a href="https://github.com/your_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/your_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/your_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/your_username/repo_name/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

The **EV Charging Prediction Model** aims to evaluate real-time or historical electric vehicle charging sessions to predict if the session will be successfully completed or fail. Built with an optimized **Gradient Boosting Classifier**, the system accounts for several variables like battery capacity, temperature, utilization rates, and more.

Key Highlights:
* 🚀 **End-to-end Pipeline**: From data ingestion, robust feature engineering to a live Flask backend serving real-time predictions.
* 🧠 **Smart Feature Engineering**: Automatically extracts datetime elements, groups temperatures into distinct categories, and computes dynamically changing variables like EV charging speed.
* 🌐 **Interactive GUI**: Fully functional frontend interface developed with HTML/CSS.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python.org]][Python-url]
* [![Flask][Flask.com]][Flask-url]
* [![Scikit-Learn][Scikit-Learn.org]][Scikit-Learn-url]
* [![Pandas][Pandas.org]][Pandas-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Follow these steps to set up the project locally on your machine.

### Prerequisites

Ensure you have Python 3.8+ installed. You'll need pip to install the required packages.
* pip
  ```sh
  python -m pip install --upgrade pip
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/your_username/repo_name.git
   ```
2. Navigate to the project directory
   ```sh
   cd repo_name
   ```
3. Install NPM packages & dependencies
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

To start the predictive modeling tool, boot up the Flask web server:

```bash
python app.py
```
Open your standard web browser and head over to `http://127.0.0.1:5000/`. Fill the required telemetry context for an EV session, and the Gradient Boosting Predictor will give you instant feedback on whether the session is likely to succeed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- PROJECT STRUCTURE -->
## Project Structure

```text
EV-Charging-Prediction/
├── templates/
│   └── index.html               # Frontend User Interface
├── app.py                       # Main Flask Application / API
├── ev.py / ev.ipynb             # ML Model Training & EDA
├── generate_data.py             # Synthetic Datasets builder
├── gradient_boosting_model.pkl  # Serialized Trained Model
├── preprocessor.pkl             # Serialized Data Pipeline
└── requirements.txt             # Python Dependencies
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/your_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/your_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/your_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/your_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/your_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/your_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/your_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/your_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/your_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/your_username/repo_name/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username

[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Flask.com]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/
[Scikit-Learn.org]: https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white
[Scikit-Learn-url]: https://scikit-learn.org/
[Pandas.org]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
