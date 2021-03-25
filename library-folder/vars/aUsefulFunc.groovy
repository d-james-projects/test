#!groovy

def funcInLibrary() {
	return 42
}

def call(def theThingPassed = "") {
	echo "This function is called aUsefulFunc"
        echo theThingPassed
	def msg = "result = " + String(funcInLibrary())
	echo msg
}

/*def funcInLibrary() {
	return 42
}*/
