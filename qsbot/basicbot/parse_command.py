import argparse

def parse_command():
    parser = argparse.ArgumentParser()

    parser.add_argument("-W", "--welcome", help="Sets the welcome message")
    parser.add_argument("-P", "--prefix", help="Sets the prefixes to use")
    parser.add_argument("-Pr", "--presence", help="Sets the discord presence")
    parser.add_argument("-F", "--filename", help="Sets the file name to be saved to")
    parser.add_argument("-R", "--react", help="Sets the number of react for role links you want")
    args = parser.parse_args()

    filename = 'basic_bot.py'

    if args.filename:
        filename = args.filename
        with open(filename, 'w+') as bot_file:
            bot_file.write('import qsbot\n\nclient = qsbot.client()\n\n')
    else:
        with open(filename, 'w+') as bot_file:
            bot_file.write('import qsbot\n\nclient = qsbot.client()\n\n')

    if args.prefix:
        prefixes = args.prefix.split()
        if len(prefixes) == 1:
            temp = "'" + prefixes[0] + "'" 
        else:
            temp = "["
            for prefix in prefixes:
                temp += ("'" + prefix + "', ")
            temp = temp[:-2]
            temp += "]"
        with open(filename, 'a') as bot_file:
            bot_file.write("client.set_prefixes(" + temp + ")\n\n")

    if args.welcome:
        with open(filename, 'a') as bot_file:
            bot_file.write("client.set_welcome_message('" + args.welcome + "')\n\n")

    if args.presence:
        with open(filename, 'a') as bot_file:
            bot_file.write("client.set_presence('" + args.presence + "')\n\n")

    if args.react:
        if args.react.isdigit():
            num = int(args.react)
            with open(filename, 'a') as bot_file:
                for x in range(num):
                    bot_file.write("client.add_reaction_for_role('reaction" + str(x) + "', 'role" + str(x) + "')\n" )



    with open(filename, 'a') as bot_file:
        bot_file.write("\nclient.run('DISCORD TOKEN')\n\n")
