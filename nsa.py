import random
import argparse

# TODO: Parse word lists from files
words = {
	"codenames_adjective": [
		"quantum",
        "loud",
	    "red",
	    "blue",
	    "green",
	    "yellow",
	    "irate",
	    "angry",
	    "peeved",
	    "happy",
	    "slimy",
	    "sleepy",
	    "junior",
	    "slicker",
	    "united",
	    "somber",
	    "bizarre",
	    "odd",
	    "weird",
	    "wrong",
	    "latent",
	    "chilly",
	    "strange",
	    "loud",
	    "silent",
	    "hopping",
	    "orange",
	    "violet",
	    "violent",
	    "desolate",
	    "lone",
	    "cold",
	    "solemn",
	    "raging",
	    "intelligent",
	    "american",
	],
	"codenames_noun": [
		"matrix",
		"wolf",
		"solace",
	    "whisper",
	    "felony",
	    "moon",
	    "sucker",
	    "penguin",
	    "waffle",
	    "maestro",
	    "night",
	    "trinity",
	    "deity",
	    "monkey",
	    "ark",
	    "squirrel",
	    "iron",
	    "bounce",
	    "farm",
	    "chef",
	    "trough",
	    "net",
	    "trawl",
	    "glee",
	    "water",
	    "spork",
	    "plow",
	    "feed",
	    "souffle",
	    "route",
	    "bagel",
	    "montana",
	    "analyst",
	    "auto",
	    "watch",
	    "photo",
	    "yard",
	    "source",
	    "monkey",
	    "seagull",
	    "toll",
	    "spawn",
	    "gopher",
	    "chipmunk",
	    "set",
	    "calendar",
	    "artist",
	    "chaser",
	    "scan",
	    "tote",
	    "beam",
	    "entourage",
	    "genesis",
	    "walk",
	    "spatula",
	    "rage",
	    "fire",
	    "master"      
	],
	"codenames_suffix": [ 
	    " {}000",
	    "-II",
	    " {}.0",
	    " rev{}",
	    "-HX",
	    " v{}",
	]
}

def parse_args():
    parser = argparse.ArgumentParser(description='Generate NSA TAO project names')

    parser.add_argument("-n", "--num", required=False, type=int, default=1, help="Number of project names to generate")

    return parser.parse_args()

def pick_random(arr):
    return arr[random.randrange(len(arr))]

def generate_tao_name():
    name = ""

    name += pick_random(words["codenames_adjective"]).upper()
    name += pick_random(words["codenames_noun"]).upper()

    # Hacky way to do 1/5
    if (random.randrange(5) == 4):
        suffix = pick_random(words["codenames_suffix"])
        suffix = suffix.format(random.randrange(1, 9))
        
        name += suffix
        

    return name

def main(args):
    for _ in range(args.num):
        print("%s" % generate_tao_name())

if __name__ == "__main__":
    main(parse_args())