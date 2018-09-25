help:
	@echo '\*\*\*HELP MENU\*\*\*'
	@echo 'To execute the script, run the following:'
	@echo 'make POP=<POPULATION_SIZE> GEN=<NUMBER_OF_GENERATIONS> MUT=<PROBABILITY_OF_MUTATION> CROSS=<PROBABILITY_OF_CROSSOVER> K=<TOURNAMENT_SIZE> TRAIN=<TRAIN_DATA_PATH> SEED=<ACTIVATE_RANDOM_SEED> ELIT=<ACTIVATE_ELITISM>'
	@echo 'For example:'
	@echo 'make run POP=50 GEN=20 MUT=0.05 CROSS=0.9 K=2 TRAIN=./input/datasets/synth1/synth1-train.csv TEST=./input/datasets/synth1/synth1-test.csv SEED=1 ELIT=1'

run:
	python3 symbolic_regression.py $(POP) $(GEN) $(MUT) $(CROSS) $(K) $(TRAIN) $(TEST) $(SEED) $(ELIT)

test:
	python3 symbolic_regression.py 50 20 0.05 0.9 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 1 1 > output/synth1.txt &
	python3 symbolic_regression.py 50 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 1 1 > output/synth2.txt &
	python3 symbolic_regression.py 50 20 0.05 0.9 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 1 1 > output/concrete.txt &
