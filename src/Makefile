help:
	@echo '\*\*\*HELP MENU\*\*\*'
	@echo 'To execute the script, run the following:'
	@echo 'make POP=<POPULATION_SIZE> GEN=<NUMBER_OF_GENERATIONS> MUT=<PROBABILITY_OF_MUTATION> CROSS=<PROBABILITY_OF_CROSSOVER> K=<TOURNAMENT_SIZE> TRAIN=<TRAIN_DATA_PATH> SEED=<ACTIVATE_RANDOM_SEED> ELIT=<ACTIVATE_ELITISM> ELITOPS=<ACTIVATE_ELITIST_OPERATORS>'
	@echo 'For example:'
	@echo 'make run POP=100 GEN=20 MUT=0.05 CROSS=0.9 K=2 TRAIN=./input/datasets/synth1/synth1-train.csv TEST=./input/datasets/synth1/synth1-test.csv SEED=0 ELIT=1 ELITOPS=1'
	@echo 'To execute the tests, run the following:'
	@echo 'chmod +x tests.sh && ./tests.sh'

run:
	python3 symbolic_regression.py $(POP) $(GEN) $(MUT) $(CROSS) $(K) $(TRAIN) $(TEST) $(SEED) $(ELIT) $(ELITOPS)

test_no_seed:
	python3 symbolic_regression.py 100 10 0.05 0.9 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 0 1 1

test_seed:
	python3 symbolic_regression.py 100 10 0.05 0.9 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 1 1 1

execute_tests:
	@echo 'Executing test suite = $(SUITE)'

	@mkdir -p output/$(SUITE)/synth2/population/
	@echo 'Executing population variation tests on Synth2...'

	@echo 'Test Synth2: POP=20 GEN=20 MUT=0.05 CROSS=0.9 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/population/test1.txt
	python3 symbolic_regression.py 20 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/population/test1.txt
	@echo 'Test Synth2: POP=100 GEN=20 MUT=0.05 CROSS=0.9 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/population/test2.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/population/test2.txt
	@echo 'Test Synth2: POP=200 GEN=20 MUT=0.05 CROSS=0.9 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/population/test3.txt
	python3 symbolic_regression.py 200 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/population/test3.txt
	@echo 'Test Synth2: POP=500 GEN=20 MUT=0.05 CROSS=0.9 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/population/test4.txt
	python3 symbolic_regression.py 500 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/population/test4.txt
	@echo 'Test Synth2: POP=1000 GEN=20 MUT=0.05 CROSS=0.9 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/population/test5.txt
	python3 symbolic_regression.py 1000 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/population/test5.txt

	@echo 'Finished population variation tests on Synth2'

	@mkdir -p output/$(SUITE)/synth2/generation/
	@echo 'Executing generation variation tests on Synth2...'

	@echo 'Test Synth2: POP=100 GEN=20 MUT=0.05 CROSS=0.9 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/generation/test1.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/generation/test1.txt
	@echo 'Test Synth2: POP=100 GEN=40 MUT=0.05 CROSS=0.9 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/generation/test2.txt
	python3 symbolic_regression.py 100 40 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/generation/test2.txt
	@echo 'Test Synth2: POP=100 GEN=60 MUT=0.05 CROSS=0.9 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/generation/test3.txt
	python3 symbolic_regression.py 100 60 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/generation/test3.txt
	@echo 'Test Synth2: POP=100 GEN=80 MUT=0.05 CROSS=0.9 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/generation/test4.txt
	python3 symbolic_regression.py 100 80 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/generation/test4.txt
	@echo 'Test Synth2: POP=100 GEN=100 MUT=0.05 CROSS=0.9 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/generation/test5.txt
	python3 symbolic_regression.py 100 100 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/generation/test5.txt

	@echo 'Finished generation variation tests on Synth2'

	@mkdir -p output/$(SUITE)/synth2/operators/
	@echo 'Executing operators variation tests on Synth2...'

	@echo 'Test Synth2: POP=100 GEN=20 MUT=0.05 CROSS=0.9 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/operators/test1.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/operators/test1.txt
	@echo 'Test Synth2: POP=100 GEN=20 MUT=0.2 CROSS=0.7 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/operators/test2.txt
	python3 symbolic_regression.py 100 20 0.2 0.7 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/operators/test2.txt
	@echo 'Test Synth2: POP=100 GEN=20 MUT=0.4 CROSS=0.6 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/operators/test3.txt
	python3 symbolic_regression.py 100 20 0.4 0.6 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/operators/test3.txt
	@echo 'Test Synth2: POP=100 GEN=20 MUT=0.6 CROSS=0.4 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/operators/test4.txt
	python3 symbolic_regression.py 100 20 0.6 0.4 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/operators/test4.txt
	@echo 'Test Synth2: POP=100 GEN=20 MUT=0.9 CROSS=0.05 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/operators/test5.txt
	python3 symbolic_regression.py 100 20 0.9 0.05 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/operators/test5.txt

	@echo 'Finished operators variation tests on Synth2'

	@mkdir -p output/$(SUITE)/synth2/tournament/
	@echo 'Executing tournament variation tests on Synth2...'

	@echo 'Test Synth2: POP=100 GEN=20 MUT=0.05 CROSS=0.9 K=1 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/tournament/test1.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 1 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/tournament/test1.txt
	@echo 'Test Synth2: POP=100 GEN=20 MUT=0.05 CROSS=0.9 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/tournament/test2.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/tournament/test2.txt
	@echo 'Test Synth2: POP=100 GEN=20 MUT=0.05 CROSS=0.9 K=4 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/tournament/test3.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 4 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/tournament/test3.txt
	@echo 'Test Synth2: POP=100 GEN=20 MUT=0.05 CROSS=0.9 K=10 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/tournament/test4.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 10 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/tournament/test4.txt
	@echo 'Test Synth2: POP=100 GEN=20 MUT=0.05 CROSS=0.9 K=50 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/tournament/test5.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 50 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/tournament/test5.txt

	@echo 'Finished tournament variation tests on Synth2'

	@mkdir -p output/$(SUITE)/synth2/elitist_operators/
	@echo 'Executing elitist operators variation tests on Synth2...'

	@echo 'Test Synth2: POP=100 GEN=20 MUT=0.05 CROSS=0.9 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/elitist_operators/test1.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/elitist_operators/test1.txt
	@echo 'Test Synth2: POP=100 GEN=20 MUT=0.05 CROSS=0.9 K=2 SEED=0 ELIT=1 ELITOPS=0' > output/$(SUITE)/synth2/elitist_operators/test2.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/elitist_operators/test2.txt

	@echo 'Finished elitist operators variation tests on Synth2'

	@mkdir -p output/$(SUITE)/synth2/elitism/
	@echo 'Executing elitism variation tests on Synth2...'

	@echo 'Test Synth2: POP=100 GEN=20 MUT=0.05 CROSS=0.9 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/synth2/elitist_operators/test1.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/elitist_operators/test1.txt
	@echo 'Test Synth2: POP=100 GEN=20 MUT=0.05 CROSS=0.9 K=2 SEED=0 ELIT=0 ELITOPS=1' > output/$(SUITE)/synth2/elitist_operators/test2.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 0 1 1 >> output/$(SUITE)/synth2/elitist_operators/test2.txt

	@echo 'Finished elitism variation tests on Synth2'


	@mkdir -p output/$(SUITE)/synth1/
	@echo 'Executing best parameters test on Synth1...'

	@echo 'Test Synth1: POP=100 GEN=50 MUT=0.4 CROSS=0.6 K=2 SEED=0 ELIT=1 ELITOPS=0' > output/$(SUITE)/synth1/test.txt
	python3 symbolic_regression.py 100 50 0.4 0.6 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 0 1 0 >> output/$(SUITE)/synth1/test.txt
	
	@echo 'Finished best parameters test on Synth1'


	@mkdir -p output/$(SUITE)/concrete/operators/
	@echo 'Executing operators variation on Concrete...'

	@echo 'Test Concrete: POP=100 GEN=50 MUT=0.4 CROSS=0.6 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/concrete/operators/test1.txt
	python3 symbolic_regression.py 100 50 0.4 0.6 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 0 1 1 >> output/$(SUITE)/concrete/operators/test1.txt
	@echo 'Test Concrete: POP=100 GEN=50 MUT=0.4 CROSS=0.6 K=2 SEED=0 ELIT=1 ELITOPS=0' > output/$(SUITE)/concrete/operators/test2.txt
	python3 symbolic_regression.py 100 50 0.4 0.6 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 0 1 0 >> output/$(SUITE)/concrete/operators/test2.txt

	@echo 'Finished operators variation on Concrete'

	@mkdir -p output/$(SUITE)/concrete/tournament/
	@echo 'Executing tournament variation on Concrete...'

	@echo 'Test Concrete: POP=100 GEN=20 MUT=0.05 CROSS=0.9 K=1 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/concrete/tournament/test1.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 1 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 0 1 1 >> output/$(SUITE)/concrete/tournament/test1.txt
	@echo 'Test Concrete: POP=100 GEN=20 MUT=0.05 CROSS=0.9 K=2 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/concrete/tournament/test2.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 0 1 1 >> output/$(SUITE)/concrete/tournament/test2.txt
	@echo 'Test Concrete: POP=100 GEN=20 MUT=0.05 CROSS=0.9 K=4 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/concrete/tournament/test3.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 4 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 0 1 1 >> output/$(SUITE)/concrete/tournament/test3.txt
	@echo 'Test Concrete: POP=100 GEN=20 MUT=0.05 CROSS=0.9 K=10 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/concrete/tournament/test4.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 10 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 0 1 1 >> output/$(SUITE)/concrete/tournament/test4.txt
	@echo 'Test Concrete: POP=100 GEN=20 MUT=0.05 CROSS=0.9 K=50 SEED=0 ELIT=1 ELITOPS=1' > output/$(SUITE)/concrete/tournament/test5.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 50 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 0 1 1 >> output/$(SUITE)/concrete/tournament/test5.txt

	@echo 'Finished tournament variation on Concrete'

	@echo 'Test suite = $(SUITE) fully generated. Check output on path ./output/$(SUITE)/'
