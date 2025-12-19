from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(test_list_0):
    assert filter_by_state(test_list_0) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date(test_list_0):
    assert sort_by_date(test_list_0) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_1(test_list_1):
    assert filter_by_state(test_list_1) == [
        {"id": 594226727, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]


def test_filter_by_state_2(test_list_1):
    assert filter_by_state(test_list_1, "CANCELED") == [
        {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"}
    ]
    assert filter_by_state(test_list_1) == [
        {"id": 594226727, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]


def test_sort_by_date_1(test_list_1):
    assert sort_by_date(test_list_1) == [
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "QWERTY", "date": "2017-12-31T02:08:58.425572"},
    ]
    assert sort_by_date(test_list_1, False) == [
        {"id": 615064591, "state": "QWERTY", "date": "2017-12-31T02:08:58.425572"},
        {"id": 939719570, "state": "", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_2(test_list_2):
    assert sort_by_date(test_list_2) == "В приведённом списке находятся операции с некорректной датой"
