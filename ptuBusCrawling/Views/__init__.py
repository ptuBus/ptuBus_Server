import ssl
from .SchoolBus.SchoolBusListView import SchoolBusListView
from .Bus.BusTerminalListView import BusTerminalListView
from .Bus.BusTimeTableListView import BusTimeTableListView
from .Train.TrainStationListView import TrainStationListView
from .Train.TrainTimeTableListView import TrainTimeTableListView

ssl._create_default_https_context = ssl._create_unverified_context
