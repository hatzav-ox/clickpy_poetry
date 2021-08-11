# noqa

# import runpy

# import clickpy
# import pytest
# from pytest import CaptureFixture
# from pytest_mock import MockerFixture


# @pytest.mark.skip("Need to rewrite this.")
# def test_run_method(mocker: MockerFixture) -> None:  # noqa
#     # Arrange
#     mock_typer = mocker.patch("clickpy.cli.typer.run")

#     # Act
#     clickpy.app()

#     # Assert
#     mock_typer.assert_called_once_with(clickpy.cli.main)


# @pytest.mark.skip("need to rewrite this.")
# def test___main__py(mocker: MockerFixture, capsys: CaptureFixture) -> None:  # noqa
#     # Arrange
#     mock_typer = mocker.patch("clickpy.cli.typer.run")
#     spy_run = mocker.spy(clickpy.cli, "main")

#     # Act
#     # use runpy to run python script like an actual script or modules
#     with pytest.raises(SystemExit) as excinfo:
#         runpy.run_module("clickpy", run_name="__main__")

#     out, err = capsys.readouterr()
#     print(out, err)
#     (retv,) = excinfo.value.args
#     # Assert
#     assert retv == 1
#     mock_typer.assert_called_once_with(clickpy.cli.main)
#     spy_run.assert_called_once()


# @pytest.mark.skip(reason="Can't figure out how to call file __main__ block.")
# def test__name_equals__main_clickpy(mocker: MockerFixture) -> None:  # noqa
#     # Arrange
#     spy_run = mocker.spy(clickpy, "run")
#     mock_typer = mocker.patch("clickpy.cli.typer.run")
#     mocker.resetall()
#     # Act
#     # runpy.run_module("clickpy", run_name="__main__")
#     runpy.run_module("clickpy.clickpy", run_name="__main__")

#     # Assert
#     mock_typer.assert_called_once_with(clickpy.cli.main)
#     spy_run.assert_called_once()
