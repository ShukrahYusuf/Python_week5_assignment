# ============================================================================
# ASSIGNMENT 1: Design Your Own Class! 🏗️
# Theme: Superhero Management System
# ============================================================================

class Superhero:
    """Base class representing a superhero with common attributes and methods."""
    
    # Class variable to keep track of total superheroes
    total_heroes = 0
    
    def __init__(self, name, real_name, power_level, primary_power):
        """Initialize a superhero with unique values."""
        self.name = name
        self.real_name = real_name
        self._power_level = power_level  # Protected attribute
        self.primary_power = primary_power
        self.is_active = True
        Superhero.total_heroes += 1
    
    # Getter and setter for power_level (encapsulation)
    @property
    def power_level(self):
        return self._power_level
    
    @power_level.setter
    def power_level(self, value):
        if 0 <= value <= 100:
            self._power_level = value
        else:
            print("Power level must be between 0 and 100!")
    
    def introduce(self):
        """Introduce the superhero."""
        return f"I am {self.name}! My real identity is {self.real_name}."
    
    def use_power(self):
        """Use the superhero's primary power."""
        return f"{self.name} uses {self.primary_power}!"
    
    def train(self):
        """Train to increase power level."""
        if self._power_level < 95:
            self._power_level += 5
            return f"{self.name} trained hard! Power level increased to {self._power_level}."
        return f"{self.name} has reached near-maximum power!"
    
    def __str__(self):
        status = "Active" if self.is_active else "Retired"
        return f"{self.name} ({self.real_name}) - Power: {self._power_level}/100 - Status: {status}"


class FlyingHero(Superhero):
    """Inherited class for superheroes who can fly."""
    
    def __init__(self, name, real_name, power_level, primary_power, max_altitude):
        super().__init__(name, real_name, power_level, primary_power)
        self.max_altitude = max_altitude
    
    def fly(self):
        """Specific method for flying heroes."""
        return f"{self.name} soars through the sky at {self.max_altitude} feet!"
    
    def use_power(self):
        """Override parent method with flying-specific power usage."""
        return f"{self.name} uses {self.primary_power} while flying majestically!"


class StrengthHero(Superhero):
    """Inherited class for superheroes with super strength."""
    
    def __init__(self, name, real_name, power_level, primary_power, lift_capacity):
        super().__init__(name, real_name, power_level, primary_power)
        self.lift_capacity = lift_capacity  # in tons
    
    def lift_heavy_object(self):
        """Specific method for strength heroes."""
        return f"{self.name} lifts up to {self.lift_capacity} tons with ease!"
    
    def use_power(self):
        """Override parent method with strength-specific power usage."""
        return f"{self.name} uses {self.primary_power} with incredible force!"


class TechHero(Superhero):
    """Inherited class for technology-based superheroes."""
    
    def __init__(self, name, real_name, power_level, primary_power, gadget_count):
        super().__init__(name, real_name, power_level, primary_power)
        self.gadget_count = gadget_count
        self.gadgets = []
    
    def add_gadget(self, gadget_name):
        """Add a new gadget to the hero's arsenal."""
        self.gadgets.append(gadget_name)
        return f"{self.name} acquired new gadget: {gadget_name}"
    
    def use_power(self):
        """Override parent method with tech-specific power usage."""
        gadget_info = f" using {len(self.gadgets)} high-tech gadgets" if self.gadgets else ""
        return f"{self.name} uses {self.primary_power}{gadget_info}!"


def demonstrate_assignment_1():
    """Demonstrate the superhero class system."""
    print("=" * 60)
    print("ASSIGNMENT 1: SUPERHERO CLASS DEMONSTRATION")
    print("=" * 60)
    
    # Create different types of superheroes
    superman = FlyingHero("Superman", "Clark Kent", 95, "Super Strength & Flight", 50000)
    batman = TechHero("Batman", "Bruce Wayne", 85, "Detective Skills & Gadgets", 50)
    hulk = StrengthHero("Hulk", "Bruce Banner", 90, "Incredible Strength", 150)
    
    # Add gadgets to Batman
    batman.add_gadget("Batarang")
    batman.add_gadget("Grappling Hook")
    batman.add_gadget("Batmobile")
    
    heroes = [superman, batman, hulk]
    
    print(f"Total heroes created: {Superhero.total_heroes}\n")
    
    # Demonstrate each hero
    for hero in heroes:
        print(f"📋 Hero Info: {hero}")
        print(f"💬 Introduction: {hero.introduce()}")
        print(f"⚡ Power Usage: {hero.use_power()}")
        
        # Demonstrate specific abilities based on type
        if isinstance(hero, FlyingHero):
            print(f"✈️  Flight: {hero.fly()}")
        elif isinstance(hero, StrengthHero):
            print(f"💪 Strength: {hero.lift_heavy_object()}")
        elif isinstance(hero, TechHero):
            print(f"🔧 Gadgets: {', '.join(hero.gadgets) if hero.gadgets else 'None'}")
        
        print(f"🏋️ Training: {hero.train()}")
        print("-" * 40)
    
    # Demonstrate encapsulation
    print("\n🔒 ENCAPSULATION DEMO:")
    print("Trying to set Superman's power level to 150 (invalid)...")
    superman.power_level = 150  # This will trigger validation
    print(f"Superman's actual power level: {superman.power_level}")


# ============================================================================
# ASSIGNMENT 2: Polymorphism Challenge! 🎭
# Theme: Transportation System
# ============================================================================

class Vehicle:
    """Base class for all vehicles."""
    
    def __init__(self, name, max_speed, fuel_type):
        self.name = name
        self.max_speed = max_speed
        self.fuel_type = fuel_type
        self.is_moving = False
    
    def move(self):
        """Base move method - to be overridden by subclasses."""
        return f"{self.name} is moving"
    
    def stop(self):
        """Common stop method for all vehicles."""
        self.is_moving = False
        return f"{self.name} has stopped"
    
    def get_info(self):
        """Get vehicle information."""
        return f"{self.name} - Max Speed: {self.max_speed} - Fuel: {self.fuel_type}"


class Car(Vehicle):
    """Car class with specific movement behavior."""
    
    def __init__(self, name, max_speed, fuel_type, doors):
        super().__init__(name, max_speed, fuel_type)
        self.doors = doors
    
    def move(self):
        """Override move method for cars."""
        self.is_moving = True
        return f"🚗 {self.name} is driving on the road at {self.max_speed} mph"
    
    def honk(self):
        """Car-specific method."""
        return f"{self.name} goes BEEP BEEP! 📯"


class Plane(Vehicle):
    """Plane class with specific movement behavior."""
    
    def __init__(self, name, max_speed, fuel_type, altitude):
        super().__init__(name, max_speed, fuel_type)
        self.max_altitude = altitude
    
    def move(self):
        """Override move method for planes."""
        self.is_moving = True
        return f"✈️ {self.name} is flying through the sky at {self.max_speed} mph"
    
    def takeoff(self):
        """Plane-specific method."""
        return f"{self.name} is taking off! Reaching {self.max_altitude} feet! 🛫"


class Boat(Vehicle):
    """Boat class with specific movement behavior."""
    
    def __init__(self, name, max_speed, fuel_type, capacity):
        super().__init__(name, max_speed, fuel_type)
        self.passenger_capacity = capacity
    
    def move(self):
        """Override move method for boats."""
        self.is_moving = True
        return f"🚢 {self.name} is sailing across the water at {self.max_speed} knots"
    
    def anchor(self):
        """Boat-specific method."""
        return f"{self.name} drops anchor! ⚓"


class Bicycle(Vehicle):
    """Bicycle class with specific movement behavior."""
    
    def __init__(self, name, max_speed, gears):
        super().__init__(name, max_speed, "Human Power")
        self.gears = gears
    
    def move(self):
        """Override move method for bicycles."""
        self.is_moving = True
        return f"🚲 {self.name} is pedaling along the path at {self.max_speed} mph"
    
    def ring_bell(self):
        """Bicycle-specific method."""
        return f"{self.name} rings its bell: RING RING! 🔔"


class Spaceship(Vehicle):
    """Spaceship class with specific movement behavior."""
    
    def __init__(self, name, max_speed, fuel_type, warp_capable):
        super().__init__(name, max_speed, fuel_type)
        self.warp_capable = warp_capable
    
    def move(self):
        """Override move method for spaceships."""
        self.is_moving = True
        warp_status = "with warp drive" if self.warp_capable else "with conventional thrusters"
        return f"🚀 {self.name} is traveling through space at {self.max_speed} mph {warp_status}"
    
    def engage_warp(self):
        """Spaceship-specific method."""
        if self.warp_capable:
            return f"{self.name} engages warp drive! WHOOSH! 🌟"
        return f"{self.name} doesn't have warp capabilities"


def demonstrate_assignment_2():
    """Demonstrate polymorphism with different vehicle types."""
    print("=" * 60)
    print("ASSIGNMENT 2: POLYMORPHISM DEMONSTRATION")
    print("=" * 60)
    
    # Create different types of vehicles
    vehicles = [
        Car("Tesla Model S", 155, "Electric", 4),
        Plane("Boeing 747", 570, "Jet Fuel", 35000),
        Boat("Yacht Paradise", 25, "Diesel", 12),
        Bicycle("Mountain Explorer", 15, 21),
        Spaceship("USS Enterprise", 186000, "Antimatter", True)
    ]
    
    print("🚦 POLYMORPHISM IN ACTION:")
    print("All vehicles using the same move() method, but behaving differently!\n")
    
    # Demonstrate polymorphism - same method call, different behaviors
    for vehicle in vehicles:
        print(f"📊 {vehicle.get_info()}")
        print(f"🎬 Action: {vehicle.move()}")  # Same method call, different implementation
        
        # Demonstrate specific methods for each vehicle type
        if isinstance(vehicle, Car):
            print(f"🔊 Sound: {vehicle.honk()}")
        elif isinstance(vehicle, Plane):
            print(f"🛫 Special: {vehicle.takeoff()}")
        elif isinstance(vehicle, Boat):
            print(f"⚓ Special: {vehicle.anchor()}")
        elif isinstance(vehicle, Bicycle):
            print(f"🔔 Sound: {vehicle.ring_bell()}")
        elif isinstance(vehicle, Spaceship):
            print(f"🌟 Special: {vehicle.engage_warp()}")
        
        print(f"🛑 Stop: {vehicle.stop()}")
        print("-" * 50)
    
    print("This is the power of polymorphism in object-oriented programming! ✨")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("🎓 OBJECT-ORIENTED PROGRAMMING ASSIGNMENT")
    print("Demonstrating Classes, Inheritance, Encapsulation & Polymorphism\n")
    
    # Run Assignment 1 demonstration
    demonstrate_assignment_1()
    
    print("\n" + "="*60 + "\n")
    
    # Run Assignment 2 demonstration
    demonstrate_assignment_2()
    
    print("\n🎉 Assignment Complete! Both challenges successfully implemented! 🎉")