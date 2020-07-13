from click.testing import CliRunner
from cli import poc

def test_cli_poc():
    runner = CliRunner()
    result = runner.invoke(poc, ['--name', 'foo'])
    assert result.exit_code == 0
    assert 'foo' in result.output
