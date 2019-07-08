# VideoTime
This repository implemented a novel approach to tackle cold-start problem for video recommender system. Currently, recommender systems heavily rely on collaborative filtering. Both user-based and content-based collaborative filtering is dependent on click/use information and user information. This led to cold-start problems for recommender systems. When a new user joined or a new piece of content is added to the platform, the recommender system can't draw any inferences on them given the limited information.

Some common approaches include: to extract user information from interviews, extract side social relationships, representatives-based method that represents users over selected representative items. The majority of these methods involves solving high-dimentional matrices. These methods usually constructs shared vector space that represents contents. Euclidean distance is assumed to represent the similarity between contents. These approaches are inherently computationaly expensive. 



## Installation

```
./setup.py install
```

Run:

```
videtime
```

## Dev setup

Setup conda environment:
```
conda create -n VideoTime python=3.7
conda activate VideoTime
```

Install dependencies:

```
conda install nwani::portaudio nwani::pyaudio
pip install -r requirements.txt
```

## Run tests

```
./setup.py test
```

## Usage

### Run locally

```
docker-compose up -d dejavu
python -m videotime.main
```

### Process new videos

```
curl localhost:5000/process -H 'content-type: application/json' --data '{"url": "https://www.youtube.com/watch?v=3dcli9i_pvA"}'
```
