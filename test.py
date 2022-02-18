import pytest


@pytest.fixture()
def dataSet():
    baseSet = {1,2,3}
    return baseSet
@pytest.fixture()
def dataStr():
    baseString = 'hello'
    return baseString

# Set tests

#positive
def testSetUniqueElements(dataSet):
    testSet = dataSet
    testSet.add(1)
    assert testSet == {1,2,3}

#negative
def testSetDivision(dataSet):
    setB = dataSet
    try:
        assert setB / 1
    except TypeError:
        pass

#params
@pytest.mark.parametrize('dataType', ['Four', (5,6), True])
def testSetAnyTypeElements(dataSet, dataType):
    testSet = dataSet
    testSet.add(dataType)
    assert testSet == {1, 2, 3, dataType}

# Str tests

#positive
def testStringConcat(dataStr):
    strA = dataStr
    strB = 'VK'
    assert strA + ' ' + strB == 'hello VK'

#negative
def testStrDivideInt(dataStr):
    strA = dataStr
    try:
        assert strA / 1
    except TypeError:
        pass

#params
@pytest.mark.parametrize('dataType', [],  ())
def testStrConversion(dataStr, dataType):
    strA = dataStr
    result = strA.split(',')
    assert type(result) == type(dataType)