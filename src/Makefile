help:
	@echo '\*\*\*HELP MENU\*\*\*'
	@echo 'To execute the script, run the following:'
	@echo 'make POP=<POPULATION_SIZE> GEN=<NUMBER_OF_GENERATIONS> MUT=<PROBABILITY_OF_MUTATION> CROSS=<PROBABILITY_OF_CROSSOVER> TRAIN=<TRAIN_DATA_PATH>'
	@echo 'For example:'
	@echo 'make run POP=50 GEN=20 MUT=0.05 CROSS=0.9 K=2 TRAIN=./input/datasets/synth1/synth1-train.csv TEST=./input/datasets/synth1/synth1-test.csv'

run:
	python3 symbolic_regression.py $(POP) $(GEN) $(MUT) $(CROSS) $(K) $(TRAIN) $(TEST)

test:
	python3 symbolic_regression.py 50 20 0.05 0.9 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv > output/synth1.txt &
	python3 symbolic_regression.py 50 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv > output/synth2.txt &
	python3 symbolic_regression.py 50 20 0.05 0.9 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv > output/concrete.txt &
