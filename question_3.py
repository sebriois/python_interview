# A rocket is assembled as legos. It
# • has a capsule/head
# • has one or several floors
# • has an engine
# • can have one or several boosters.
#
# Several types of capsules/heads and engines exist.
# List of available capsules
# • capsuleC for crew
# • capsuleP for payload
#
# List of available engines
# • supraluminal engine
# • ionic engine
# • combustion engine
#
# A floor has a content and 2 connectors: top and bottom.
# • The top connector can link another floor or a capsule.
# • The bottom connector can link another floor or an engine.
#
# An engine can be connected to one or several boosters.
# The ignition and extinction for each engine type is different.
#
# A rocket accepts 3 actions:
# • launching: ignition of the engine is required
# • landing: ignition of the engine is required
# • holding orbit: extinction of the engine is required
#

# Task:
# Design the skeleton of a program to model the assembling and the use of a rocket.
# • create one rocket with a capsuleP, 1 floor and a supraluminic engine. Launch the rocket.
# • create one rocket with a capsuleC, 3 floors, an ionic engine. Land the rocket.

class Rocket(object):

    def __init__(self):
        self.id = id
        self.rocket_parts = []

    def get_id(self):
        return self.id

    @staticmethod
    def create_from_rocket_parts(rocket_parts):
        rocket = Rocket()
        for part in rocket_parts:
            if part.has_top_connector() or part.has_bottom_connector():
                raise Exception("This part is already connected")
            else:
                rocket.add_rocket_part(part)
        return rocket

    def add_rocket_part(self, part):
        if not isinstance(part, RocketPart):
            raise TypeError("Part must be of type RocketPart")
        else:
            if not self.rocket_parts:
                if not isinstance(part, Capsule):
                    raise TypeError("First part must be a capsule")
                else:
                    self.rocket_parts.append(part)
            else:
                last_part = self.rocket_parts[-1]
                last_part.set_bottom_connector(part)
                part.set_top_connector(last_part)
                self.rocket_parts.append(part)
        return self

    def is_valid(self):
        has_capsule = False
        has_floors = False
        has_engines = False
        has_boosters = False
        for part in self.rocket_parts:
            if isinstance(part, Capsule):
                has_capsule = True
            if isinstance(part, Floor):
                has_floors = True
            if isinstance(part, Engine):
                has_engines = True
            if isinstance(part, Booster):
                has_boosters = True
        return has_capsule and has_floors and has_engines and has_boosters

    def start_engine(self):
        for part in self.rocket_parts:
            if isinstance(part, Engine):
                part.ignition()

    def stop_engine(self):
        for part in self.rocket_parts:
            if isinstance(part, Engine):
                part.extinction()

    def launch_rocket(self):
        if self.is_valid():
            self.start_engine()
        else:
            raise Exception("Your rocket will blow up")

    def hold_rocket(self):
        self.stop_engine()

    def land_rocket(self):
        self.start_engine()

    def __repr__(self):
        res = ""
        for part in self.rocket_parts:
            res += " -- " + str(part)
        return res


class RocketPart:

    def __init__(self):
        self.top_connector = None
        self.bottom_connector = None

    def get_top_connector(self):
        return self.top_connector

    def set_top_connector(self, connector):
        if not isinstance(connector, RocketPart):
            raise TypeError("Connector must be of type RocketPart")
        self.top_connector = connector

    def get_bottom_connector(self):
        return self.bottom_connector

    def set_bottom_connector(self, connector):
        if not isinstance(connector, RocketPart):
            raise TypeError("Connector must be of type RocketPart")
        self.bottom_connector = connector

    def has_top_connector(self):
        return self.top_connector is not None

    def has_bottom_connector(self):
        return self.bottom_connector is not None


class Capsule(RocketPart):

    def get_name(self):
        raise NotImplementedError("Subclass should implement this")

    def get_description(self):
        raise NotImplementedError("Subclass should implement this")

    def set_top_connector(self, connector):
        raise Exception("Capsules can't have a top connector")

    def set_bottom_connector(self, connector):
        if not isinstance(connector, Floor):
            raise TypeError("Capsules only accept floors through a connector")
        super().set_bottom_connector(connector)


class CapsuleC(Capsule):
    def get_name(self):
        return "CapsuleC"

    def get_description(self):
        return "Capsule for crew"


class CapsuleP(Capsule):
    def get_name(self):
        return "CapsuleP"

    def get_description(self):
        return "Capsule for payload"


class Floor(RocketPart):

    def __init__(self):
        super().__init__()
        self.content = []

    def get_content(self):
        return self.content

    def set_content(self, content):
        if not isinstance(content, list):
            return Exception("Element is not a list type")
        self.content = content

    def set_top_connector(self, connector):
        if not isinstance(connector, Capsule) and not isinstance(connector, Floor):
            raise Exception("Capsule can't have an engine as a top connector")
        super().set_top_connector(connector)

    def set_bottom_connector(self, connector):
        if not isinstance(connector, Engine) and not isinstance(connector, Floor):
            raise Exception("Capsule can't have a capsule as a top connector")
        super().set_bottom_connector(connector)


class Engine(RocketPart):

    def get_name(self):
        raise NotImplementedError("No engine was selected")

    def ignition(self):
        raise NotImplementedError("No ignition method was implemented")

    def extinction(self):
        raise NotImplementedError("No extinction method was implemented")

    def set_top_connector(self, connector):
        if not isinstance(connector, Floor):
            raise TypeError("Engines only accept floors through a connector")
        super().set_top_connector(connector)

    def set_bottom_connector(self, connector):
        if not isinstance(connector, Booster):
            raise TypeError("Engines only accept booster through a bottom connector")
        super().set_bottom_connector(connector)


class SupraluminalEngine(Engine):
    def get_name(self):
        return "Supraluminal Engine"

    def ignition(self):
        pass

    def extinction(self):
        pass


class IonicEngine(Engine):
    def get_name(self):
        return "Ionic Engine"

    def ignition(self):
        pass

    def extinction(self):
        pass


class CombustionEngine(Engine):
    def get_name(self):
        return "Combustion Engine"

    def ignition(self):
        pass

    def extinction(self):
        pass


class Booster(RocketPart):
    def set_top_connector(self, connector):
        if not isinstance(connector, Engine):
            raise TypeError("Boosters only accept engines through a connector")
        super().set_top_connector(connector)

    def set_bottom_connector(self, connector):
        raise Exception("Boosters can't have a bottom connector")


rocket_1 = Rocket()
rocket_1.add_rocket_part(CapsuleP()).add_rocket_part(Floor()).add_rocket_part(SupraluminalEngine()).\
    add_rocket_part(Booster())
print(rocket_1)
rocket_1.launch_rocket()

rocket_2 = Rocket()
rocket_2.add_rocket_part(CapsuleC()).add_rocket_part(Floor()).add_rocket_part(Floor()).add_rocket_part(Floor()).\
    add_rocket_part(IonicEngine()).add_rocket_part(Booster())
print(rocket_2)
# OR
rocket_2 = Rocket.create_from_rocket_parts([CapsuleC(), Floor(), Floor(), Floor(), IonicEngine(), Booster()])
print(rocket_2)
rocket_2.launch_rocket()
rocket_2.hold_rocket()
rocket_2.land_rocket()

