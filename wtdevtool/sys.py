import click
import platform
import os

def get_os():
    if platform.system() == 'Linux':
        ver = platform.version().lower()

        if ver.find('nixos'):
            return 'nixos'
    return 'unknown'

@click.command()
def lsrollback():
    if get_os() == 'nixos':
        print('--==[System profiles]==--')
        os.system('ls /nix/var/nix/profiles/system* -lah')
        print('')
        print('--==[User profiles]==--')
        os.system('ls /nix/var/nix/profiles/per-user/' + os.environ['USER'] + ' -lah')
        print('')

@click.command()
def clean():
    if get_os() == 'nixos':
        print('Running Garbage Collection')
        os.system('nix-store --gc')
        print('Deduplication running...this may take awhile')
        os.system('nix-store --optimise')


@click.command()
def update():

    if get_os() == 'nixos':
        current_dir = os.getcwd()
        os.chdir(os.environ['HOME'] + '/.dotfiles')
        os.system('sudo ~/.dotfiles/update.sh')
        os.chdir(current_dir)
    else:
        click.echo('Unknown platform. Unable to update')

@click.command()
def install():
    if get_os() == 'nixos':
        click.echo('You are in NixOS! Please add the package to your config or devshell!')
    else:
        click.echo('Unknown platform. Unable to install package')

@click.command()
def uninstall():
    if get_os() == 'nixos':
        click.echo('You are in NixOS! Please remove the package from your config or devshell!')
    else:
        click.echo('Unknown platform. Unable to install package')


@click.command()
@click.argument('query')
def search(query):
    if get_os() == 'nixos':
        os.system('nix search nixpkgs ' + query)
    else:
        click.echo('Unknown platform. Unable to search for package')

@click.command()
@click.argument('query')
def find(query):
    if get_os() == 'nixos':
        os.system('nix search nixpkgs ' + query)
    else:
        click.echo('Unknown platform. Unable to search for package')

@click.command()
def apply():
    if get_os() == 'nixos':
        current_dir = os.getcwd()
        os.chdir(os.environ['HOME'] + '/.dotfiles')
        os.system('sudo ~/.dotfiles/apply.sh')
        os.chdir(current_dir)
@click.command()
def info():
    os.system('neofetch')


@click.group()
def cli():
    pass


cli.add_command(install)
cli.add_command(uninstall)
cli.add_command(update)
cli.add_command(search)
cli.add_command(find)
cli.add_command(info)
cli.add_command(apply)
cli.add_command(clean)
cli.add_command(lsrollback)

#if __name__ == '__main__':
#    cli()
