#!groovy

def call(def theThingPassed = "") {
	echo "This function is called aUsefulFunc"
        echo theThingPassed
	echo funcInLibrary
}

def funcInLibrary() {
	return 42
}
