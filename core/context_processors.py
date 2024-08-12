def header_variables(request):
    # Get the full name of the logged-in user
    full_name = "Guest User"
    if request.user.is_authenticated:
        full_name = request.user.get_full_name()
    
    # Return a dictionary with the full name
    return {
        'full_name': full_name,
    }

def exercise_choices(request):
    EXERCISE_CHOICES = {
    'Backa': 'Back: Deadlifts',
    'Backb': 'Back: Pull-ups',
    'Backc': 'Back: Barbell rows',
    'Backd': 'Back: Lat pulldowns',
    'Backe': 'Back: Single-arm dumbbell rows',
    'Backf': 'Back: T-bar rows',
    'Backg': 'Back: Seated cable rows',
    'Backh': 'Back: Dumbbell pullovers',
    'Backi': 'Back: Bent-over dumbbell rows',
    'Backj': 'Back: Hyperextensions',
    'Chesta': 'Chest: Bench press (barbell or dumbbell)',
    'Chestb': 'Chest: Push-ups',
    'Chestc': 'Chest: Incline bench press',
    'Chestd': 'Chest: Chest flyes (cable or dumbbell)',
    'Cheste': 'Chest: Decline bench press',
    'Chestf': 'Chest: Dumbbell pullovers',
    'Chestg': 'Chest: Dips (chest variation)',
    'Chesth': 'Chest: Cable crossovers',
    'Chesti': 'Chest: Machine chest press',
    'Chestj': 'Chest: Incline dumbbell press',
    'Shouldersa': 'Shoulders: Overhead press (barbell or dumbbell)',
    'Shouldersb': 'Shoulders: Dumbbell lateral raises',
    'Shouldersc': 'Shoulders: Front dumbbell raises',
    'Shouldersd': 'Shoulders: Arnold press',
    'Shoulderse': 'Shoulders: Upright rows',
    'Shouldersf': 'Shoulders: Shoulder press machine',
    'Shouldersg': 'Shoulders: Cable lateral raises',
    'Shouldersh': 'Shoulders: Reverse flyes (dumbbell or machine)',
    'Shouldersi': 'Shoulders: Face pulls',
    'Shouldersj': 'Shoulders: Shrugs (barbell or dumbbell)',
    'Legsa': 'Legs: Squats (barbell or dumbbell)',
    'Legsb': 'Legs: Lunges (forward, reverse, or walking)',
    'Legsc': 'Legs: Leg press',
    'Legsd': 'Legs: Deadlifts (conventional or sumo)',
    'Legse': 'Legs: Leg extensions',
    'Legsf': 'Legs: Leg curls (standing or lying)',
    'Legsg': 'Legs: Calf raises (seated or standing)',
    'Legsh': 'Legs: Bulgarian split squats',
    'Legsi': 'Legs: Box jumps',
    'Legsj': 'Legs: Romanian deadlifts',
    'Bicepsa': 'Biceps: Barbell curls',
    'Bicepsb': 'Biceps: Dumbbell curls (standing or seated)',
    'Bicepsc': 'Biceps: Preacher curls (barbell or dumbbell)',
    'Bicepsd': 'Biceps: Hammer curls',
    'Bicepse': 'Biceps: Concentration curls',
    'Bicepsf': 'Biceps: Cable curls',
    'Bicepsg': 'Biceps: Incline dumbbell curls',
    'Bicepsh': 'Biceps: Reverse curls',
    'Bicepsi': 'Biceps: EZ-bar curls',
    'Bicepsj': 'Biceps: Spider curls',
    'Tricepsa': 'Triceps: Tricep dips (parallel bars or bench)',
    'Tricepsb': 'Triceps: Close-grip bench press',
    'Tricepsc': 'Triceps: Tricep pushdowns (cable machine)',
    'Tricepsd': 'Triceps: Skull crushers (barbell or dumbbell)',
    'Tricepse': 'Triceps: Overhead tricep extensions (dumbbell or cable)',
    'Tricepsf': 'Triceps: Tricep kickbacks',
    'Tricepsg': 'Triceps: Diamond push-ups',
    'Tricepsh': 'Triceps: Rope tricep pushdowns',
    'Tricepsi': 'Triceps: Bench dips',
    'Tricepsj': 'Triceps: Tricep rope overhead extension',
    'Absa': 'Abs: Crunches (standard, reverse, or bicycle)',
    'Absb': 'Abs: Planks (standard, side, or weighted)',
    'Absc': 'Abs: Russian twists',
    'Absd': 'Abs: Leg raises (lying or hanging)',
    'Abse': 'Abs: Mountain climbers',
    'Absf': 'Abs: Cable crunches',
    'Absg': 'Abs: Woodchoppers (cable or medicine ball)',
    'Absh': 'Abs: Ab wheel rollouts',
    'Absi': 'Abs: Hanging knee raises',
    'Absj': 'Abs: Flutter kicks',
    }

    EXERCISE_CHOICES_SPLIT = {
        key: value.split(': ', 1)  # Split on the first occurrence of ': '
        for key, value in EXERCISE_CHOICES.items()
    }

    return {'exercise_choices': EXERCISE_CHOICES_SPLIT}   
