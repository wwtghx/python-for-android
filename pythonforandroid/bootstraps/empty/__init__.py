from pythonforandroid.toolchain import Bootstrap


class EmptyBootstrap(Bootstrap):
    name = 'empty'

    recipe_depends = []

    can_be_chosen_automatically = False

    def run_distribute(self):
        print('empty bootstrap has no distribute')
        exit(1)


bootstrap = EmptyBootstrap()
