help:
	@echo '\*\*\*HELP MENU\*\*\*'
	@echo 'To execute the script, run the following:'
	@echo 'make POP=<POPULATION_SIZE> GEN=<NUMBER_OF_GENERATIONS> MUT=<PROBABILITY_OF_MUTATION> CROSS=<PROBABILITY_OF_CROSSOVER> K=<TOURNAMENT_SIZE> TRAIN=<TRAIN_DATA_PATH> SEED=<ACTIVATE_RANDOM_SEED> ELIT=<ACTIVATE_ELITISM> ELITOPS=<ACTIVATE_ELITIST_OPERATORS>'
	@echo 'For example:'
	@echo 'make run POP=50 GEN=20 MUT=0.05 CROSS=0.9 K=2 TRAIN=./input/datasets/synth1/synth1-train.csv TEST=./input/datasets/synth1/synth1-test.csv SEED=1 ELIT=1 ELITOPS=1'

run:
	python3 symbolic_regression.py $(POP) $(GEN) $(MUT) $(CROSS) $(K) $(TRAIN) $(TEST) $(SEED) $(ELIT) $(ELITOPS)

test_no_seed:
	python3 symbolic_regression.py 100 10 0.05 0.9 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 0 1 1

test_seed:
	python3 symbolic_regression.py 100 10 0.05 0.9 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 1 1 1

execute_tests:
	echo 'Test Synth1: POP=100 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=1 ELITOPERATORS=1' > output/test1.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 1 1 1 >> output/test1.txt &
	echo 'Test Synth2: POP=100 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=1 ELITOPERATORS=1' > output/test2.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 1 1 1 >> output/test2.txt &
	echo 'Test Concrete: POP=100 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=1 ELITOPERATORS=1' > output/test3.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 1 1 1 >> output/test3.txt &
	echo 'Test Synth1: POP=100 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=0 ELITOPERATORS=1' > output/test4.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 1 0 1 >> output/test4.txt &
	echo 'Test Synth2: POP=100 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=0 ELITOPERATORS=1' > output/test5.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 1 0 1 >> output/test5.txt &
	echo 'Test Concrete: POP=100 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=0 ELITOPERATORS=1' > output/test6.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 1 0 1 >> output/test6.txt &
	echo 'Test Synth1: POP=100 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=1 ELITOPERATORS=0' > output/test7.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 1 1 0 >> output/test7.txt &
	echo 'Test Synth2: POP=100 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=1 ELITOPERATORS=0' > output/test8.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 1 1 0 >> output/test8.txt &
	echo 'Test Concrete: POP=100 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=1 ELITOPERATORS=0' > output/test9.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 1 1 0 >> output/test9.txt &
	echo 'Test Synth1: POP=100 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=0 ELITOPERATORS=0' > output/test10.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 1 0 0 >> output/test10.txt &
	echo 'Test Synth2: POP=100 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=0 ELITOPERATORS=0' > output/test11.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 1 0 0 >> output/test11.txt &
	echo 'Test Concrete: POP=100 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=0 ELITOPERATORS=0' > output/test12.txt
	python3 symbolic_regression.py 100 20 0.05 0.9 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 1 0 0 >> output/test12.txt

	echo 'Test Synth1: POP=100 GEN=20 MUT=0.4 CROSS=0.6 SEED=1 ELISTIM=1 ELITOPERATORS=1' > output/test13.txt
	python3 symbolic_regression.py 100 20 0.4 0.6 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 1 1 1 >> output/test13.txt &
	echo 'Test Synth2: POP=100 GEN=20 MUT=0.4 CROSS=0.6 SEED=1 ELISTIM=1 ELITOPERATORS=1' > output/test14.txt
	python3 symbolic_regression.py 100 20 0.4 0.6 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 1 1 1 >> output/test14.txt &
	echo 'Test Concrete: POP=100 GEN=20 MUT=0.4 CROSS=0.6 SEED=1 ELISTIM=1 ELITOPERATORS=1' > output/test15.txt
	python3 symbolic_regression.py 100 20 0.4 0.6 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 1 1 1 >> output/test15.txt &
	echo 'Test Synth1: POP=100 GEN=20 MUT=0.4 CROSS=0.6 SEED=1 ELISTIM=0 ELITOPERATORS=1' > output/test16.txt
	python3 symbolic_regression.py 100 20 0.4 0.6 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 1 0 1 >> output/test16.txt &
	echo 'Test Synth2: POP=100 GEN=20 MUT=0.4 CROSS=0.6 SEED=1 ELISTIM=0 ELITOPERATORS=1' > output/test17.txt
	python3 symbolic_regression.py 100 20 0.4 0.6 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 1 0 1 >> output/test17.txt &
	echo 'Test Concrete: POP=100 GEN=20 MUT=0.4 CROSS=0.6 SEED=1 ELISTIM=0 ELITOPERATORS=1' > output/test18.txt
	python3 symbolic_regression.py 100 20 0.4 0.6 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 1 0 1 >> output/test18.txt &
	echo 'Test Synth1: POP=100 GEN=20 MUT=0.4 CROSS=0.6 SEED=1 ELISTIM=1 ELITOPERATORS=0' > output/test19.txt
	python3 symbolic_regression.py 100 20 0.4 0.6 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 1 1 0 >> output/test19.txt &
	echo 'Test Synth2: POP=100 GEN=20 MUT=0.4 CROSS=0.6 SEED=1 ELISTIM=1 ELITOPERATORS=0' > output/test20.txt
	python3 symbolic_regression.py 100 20 0.4 0.6 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 1 1 0 >> output/test20.txt &
	echo 'Test Concrete: POP=100 GEN=20 MUT=0.4 CROSS=0.6 SEED=1 ELISTIM=1 ELITOPERATORS=0' > output/test21.txt
	python3 symbolic_regression.py 100 20 0.4 0.6 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 1 1 0 >> output/test21.txt &
	echo 'Test Synth1: POP=100 GEN=20 MUT=0.4 CROSS=0.6 SEED=1 ELISTIM=0 ELITOPERATORS=0' > output/test22.txt
	python3 symbolic_regression.py 100 20 0.4 0.6 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 1 0 0 >> output/test22.txt &
	echo 'Test Synth2: POP=100 GEN=20 MUT=0.4 CROSS=0.6 SEED=1 ELISTIM=0 ELITOPERATORS=0' > output/test23.txt
	python3 symbolic_regression.py 100 20 0.4 0.6 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 1 0 0 >> output/test23.txt &
	echo 'Test Concrete: POP=100 GEN=20 MUT=0.4 CROSS=0.6 SEED=1 ELISTIM=0 ELITOPERATORS=0' > output/test24.txt
	python3 symbolic_regression.py 100 20 0.4 0.6 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 1 0 0 >> output/test24.txt

	echo 'Test Synth1: POP=500 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=1 ELITOPERATORS=1' > output/test25.txt
	python3 symbolic_regression.py 500 20 0.05 0.9 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 1 1 1 >> output/test25.txt &
	echo 'Test Synth2: POP=500 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=1 ELITOPERATORS=1' > output/test26.txt
	python3 symbolic_regression.py 500 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 1 1 1 >> output/test26.txt &
	echo 'Test Concrete: POP=500 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=1 ELITOPERATORS=1' > output/test27.txt
	python3 symbolic_regression.py 500 20 0.05 0.9 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 1 1 1 >> output/test27.txt &
	echo 'Test Synth1: POP=500 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=0 ELITOPERATORS=1' > output/test28.txt
	python3 symbolic_regression.py 500 20 0.05 0.9 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 1 0 1 >> output/test28.txt &
	echo 'Test Synth2: POP=500 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=0 ELITOPERATORS=1' > output/test29.txt
	python3 symbolic_regression.py 500 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 1 0 1 >> output/test29.txt &
	echo 'Test Concrete: POP=500 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=0 ELITOPERATORS=1' > output/test30.txt
	python3 symbolic_regression.py 500 20 0.05 0.9 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 1 0 1 >> output/test30.txt &
	echo 'Test Synth1: POP=500 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=1 ELITOPERATORS=0' > output/test31.txt
	python3 symbolic_regression.py 500 20 0.05 0.9 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 1 1 0 >> output/test31.txt &
	echo 'Test Synth2: POP=500 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=1 ELITOPERATORS=0' > output/test32.txt
	python3 symbolic_regression.py 500 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 1 1 0 >> output/test32.txt &
	echo 'Test Concrete: POP=500 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=1 ELITOPERATORS=0' > output/test33.txt
	python3 symbolic_regression.py 500 20 0.05 0.9 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 1 1 0 >> output/test33.txt &
	echo 'Test Synth1: POP=500 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=0 ELITOPERATORS=0' > output/test34.txt
	python3 symbolic_regression.py 500 20 0.05 0.9 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 1 0 0 >> output/test34.txt &
	echo 'Test Synth2: POP=500 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=0 ELITOPERATORS=0' > output/test35.txt
	python3 symbolic_regression.py 500 20 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 1 0 0 >> output/test35.txt &
	echo 'Test Concrete: POP=500 GEN=20 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=0 ELITOPERATORS=0' > output/test36.txt
	python3 symbolic_regression.py 500 20 0.05 0.9 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 1 0 0 >> output/test36.txt

	echo 'Test Synth1: POP=100 GEN=100 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=1 ELITOPERATORS=1' > output/test37.txt
	python3 symbolic_regression.py 100 100 0.05 0.9 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 1 1 1 >> output/test37.txt &
	echo 'Test Synth2: POP=100 GEN=100 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=1 ELITOPERATORS=1' > output/test38.txt
	python3 symbolic_regression.py 100 100 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 1 1 1 >> output/test38.txt &
	echo 'Test Concrete: POP=100 GEN=100 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=1 ELITOPERATORS=1' > output/test39.txt
	python3 symbolic_regression.py 100 100 0.05 0.9 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 1 1 1 >> output/test39.txt &
	echo 'Test Synth1: POP=100 GEN=100 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=0 ELITOPERATORS=1' > output/test40.txt
	python3 symbolic_regression.py 100 100 0.05 0.9 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 1 0 1 >> output/test40.txt &
	echo 'Test Synth2: POP=100 GEN=100 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=0 ELITOPERATORS=1' > output/test41.txt
	python3 symbolic_regression.py 100 100 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 1 0 1 >> output/test41.txt &
	echo 'Test Concrete: POP=100 GEN=100 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=0 ELITOPERATORS=1' > output/test42.txt
	python3 symbolic_regression.py 100 100 0.05 0.9 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 1 0 1 >> output/test42.txt &
	echo 'Test Synth1: POP=100 GEN=100 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=1 ELITOPERATORS=0' > output/test43.txt
	python3 symbolic_regression.py 100 100 0.05 0.9 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 1 1 0 >> output/test43.txt &
	echo 'Test Synth2: POP=100 GEN=100 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=1 ELITOPERATORS=0' > output/test44.txt
	python3 symbolic_regression.py 100 100 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 1 1 0 >> output/test44.txt &
	echo 'Test Concrete: POP=100 GEN=100 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=1 ELITOPERATORS=0' > output/test45.txt
	python3 symbolic_regression.py 100 100 0.05 0.9 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 1 1 0 >> output/test45.txt &
	echo 'Test Synth1: POP=100 GEN=100 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=0 ELITOPERATORS=0' > output/test46.txt
	python3 symbolic_regression.py 100 100 0.05 0.9 2 ./input/datasets/synth1/synth1-train.csv ./input/datasets/synth1/synth1-test.csv 1 0 0 >> output/test46.txt &
	echo 'Test Synth2: POP=100 GEN=100 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=0 ELITOPERATORS=0' > output/test47.txt
	python3 symbolic_regression.py 100 100 0.05 0.9 2 ./input/datasets/synth2/synth2-train.csv ./input/datasets/synth2/synth2-test.csv 1 0 0 >> output/test47.txt &
	echo 'Test Concrete: POP=100 GEN=100 MUT=0.05 CROSS=0.9 SEED=1 ELISTIM=0 ELITOPERATORS=0' > output/test48.txt
	python3 symbolic_regression.py 100 100 0.05 0.9 2 ./input/datasets/concrete/concrete-train.csv ./input/datasets/concrete/concrete-test.csv 1 0 0 >> output/test48.txt
