#!groovy

def methodA() {
	return 42
}

def methodB(def theThingPassed = "") {
	echo "This function is called methodB"
        echo theThingPassed
}

return this
