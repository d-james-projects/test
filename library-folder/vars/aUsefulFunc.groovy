#!groovy

/*def funcInLibrary() {
	return 42
}*/

def call(def theThingPassed = "") {
	echo "This function is called aUsefulFunc"
        echo theThingPassed
	def msg = "result = " + funcInLibrary().toString()
	echo msg
	echo funcInLibrary.toString()
}

def funcInLibrary() {
	return 42
}
