#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : MeUtils.
# @File         : __init__.py
# @Time         : 2021/1/31 10:20 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : python meutils/clis/__init__.py


import typer

from meutils.pipe import *

cli = typer.Typer(name="AppZoo CLI")


def _run_cmd(cmd, nohup=0):
    cmd = f"nohup {cmd} &" if nohup else cmd
    logger.debug(cmd)
    return os.system(cmd)


@cli.command(help="help")  # help会覆盖docstring
def clitest(name: str):
    """

    @param name: name
    @return:
    """
    typer.echo(f"Hello {name}")


@cli.command()
def run(app_file: str, app='fastapi', port=9955, nohup=0):
    """Support fastapi/streamlit/gradio/gui app."""
    if not Path(app_file).exists():
        app_file = Path(get_module_path(f'../apps_{app}', __file__)) / app_file

    if app in ('fastapi', 'gui', 'gradio'):
        cmd = f"python {app_file}"
    elif app == 'streamlit':
        cmd = f"streamlit run {app_file} --server.baseUrlPath web --server.port {port}"
    else:
        cmd = "echo 无app可用"

    _run_cmd(cmd, nohup)


if __name__ == '__main__':
    cli()
