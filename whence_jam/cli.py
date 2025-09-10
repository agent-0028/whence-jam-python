"""Command line interface for whence-jam."""

import click


@click.group()
@click.version_option(version="0.1.0", prog_name="whence-jam")
def main() -> None:
    """An app for knowing who recommended a song or album."""
    pass


@main.command()
@click.argument("song")
@click.argument("person")
def add(song: str, person: str) -> None:
    """Add a music recommendation."""
    click.echo(f"Adding recommendation: '{song}' recommended by {person}")
    # TODO: Implement actual functionality


@main.command()
def list() -> None:
    """List all music recommendations."""
    click.echo("Listing all recommendations:")
    # TODO: Implement actual functionality


if __name__ == "__main__":
    main()