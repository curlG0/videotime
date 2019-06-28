# VideoMe

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