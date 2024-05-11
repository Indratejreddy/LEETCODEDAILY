def goal(Body, Mind, Spirit, Heart, Code):
    while Alive:
        try:
            if Body and Mind and Spirit and Heart and Code:
                print("Body of an Athlete, 
                         Mind of a Stoic, 
                         Spirit of a Warrior,
                         Heart of a Poet, 
                         and code like Linus Torvalds—that's the goal.")
            
            if Body:
                print("Body of an Athlete")
            if Mind:
                print("Mind of a Stoic")
            if Spirit:
                print("Spirit of a Warrior")
            if Heart:
                print("Heart of a Poet")
            if Code:
                print("Code like Linus Torvalds")
            
            else:
                raise yourNotLivingUptoFullPotential
        except yourNotLivingUptoFullPotential as e:
            print("Try again and live up to full potential:", e)
        finally:

            print("That's the goal")

# Call the function to initiate the loop
goal(Alive,Body, Mind, Spirit, Heart, Code)
