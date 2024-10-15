import pytest
from pregunta3 import Simulador
from io import StringIO


def test_simulador_error(capsys):
    sim = Simulador()
    sim.define("INVALIDO", ["TestProgram", "LOCAL"])
    sim.executable("TestProgram")
    captured = capsys.readouterr()
    assert "Error: Tipo inválido 'INVALIDO'." in captured.out


def test_define_programa():
    sim = Simulador()
    sim.define("PROGRAMA", ["TestProgram", "Python"])
    assert "TestProgram" in sim.programas
    assert sim.programas["TestProgram"].nombre == "TestProgram"
    assert sim.programas["TestProgram"].lenguaje == "Python"


def test_define_programa_error():
    sim = Simulador()
    with pytest.raises(ValueError):
        sim.define("PROGRAMA", ["TestProgram", "123!@#"])


def test_define_interprete():
    sim = Simulador()
    sim.define("INTERPRETE", ["Python", "JavaScript"])
    assert "JavaScript" in sim.interpretadores
    assert sim.interpretadores["JavaScript"].lenguaje_base == "Python"
    assert sim.interpretadores["JavaScript"].lenguaje == "JavaScript"


def test_define_interprete_error_lenguaje_base():
    sim = Simulador()
    with pytest.raises(ValueError):
        sim.define("INTERPRETE", ["123!@#", "JavaScript"])


def test_define_interprete_error_lenguaje():
    sim = Simulador()
    with pytest.raises(ValueError):
        sim.define("INTERPRETE", ["Python", "123!@#"])


def test_define_traductor():
    sim = Simulador()
    sim.define("TRADUCTOR", ["Python", "JavaScript", "Ruby"])
    assert "JavaScript" in sim.traductores
    assert sim.traductores["JavaScript"].lenguaje_base == "Python"
    assert sim.traductores["JavaScript"].lenguaje_origen == "JavaScript"
    assert sim.traductores["JavaScript"].lenguaje_destino == "Ruby"


def test_define_traductor_error_lenguaje_base():
    sim = Simulador()
    with pytest.raises(ValueError):
        sim.define("TRADUCTOR", ["123!@#", "JavaScript", "Ruby"])


def test_define_traductor_error_lenguaje_origen():
    sim = Simulador()
    with pytest.raises(ValueError):
        sim.define("TRADUCTOR", ["Python", "123!@#", "Ruby"])


def test_define_traductor_error_lenguaje_destino():
    sim = Simulador()
    with pytest.raises(ValueError):
        sim.define("TRADUCTOR", ["Python", "JavaScript", "123!@#"])


def test_executable_programa_local(capsys):
    sim = Simulador()
    sim.define("PROGRAMA", ["TestProgram", "LOCAL"])
    sim.executable("TestProgram")
    captured = capsys.readouterr()
    assert "Si, es posible ejecutar el programa 'TestProgram'." in captured.out


def test_executable_programa_interprete(capsys):
    sim = Simulador()
    sim.define("INTERPRETE", ["LOCAL", "Python"])
    sim.define("PROGRAMA", ["TestProgram", "Python"])
    sim.executable("TestProgram")
    captured = capsys.readouterr()
    assert "Si, es posible ejecutar el programa 'TestProgram'." in captured.out


def test_executable_programa_interprete_recursive(capsys):
    sim = Simulador()
    sim.define("INTERPRETE", ["LOCAL", "Python"])
    sim.define("INTERPRETE", ["Python", "Java"])
    sim.define("PROGRAMA", ["TestProgram", "Java"])
    sim.executable("TestProgram")
    captured = capsys.readouterr()
    assert "Si, es posible ejecutar el programa 'TestProgram'." in captured.out


def test_executable_programa_traductor_trivial(capsys):
    sim = Simulador()
    sim.define("TRADUCTOR", ["LOCAL", "C", "LOCAL"])
    sim.define("PROGRAMA", ["TestProgram", "C"])
    sim.executable("TestProgram")
    captured = capsys.readouterr()
    assert "Si, es posible ejecutar el programa 'TestProgram'." in captured.out


def test_executable_programa_traductor_error(capsys):
    sim = Simulador()
    sim.define("INTERPRETE", ["LOCAL", "Python"])
    sim.define("TRADUCTOR", ["Python", "JavaScript", "Ruby"])
    sim.define("PROGRAMA", ["TestProgram", "JavaScript"])
    sim.executable("TestProgram")
    captured = capsys.readouterr()
    assert "No es posible ejecutar el programa 'TestProgram'." in captured.out


def test_executable_programa_interpreter_error(capsys):
    sim = Simulador()
    sim.define("INTERPRETE", ["Python", "C"])
    sim.define("PROGRAMA", ["TestProgram", "C"])
    sim.executable("TestProgram")
    captured = capsys.readouterr()
    assert "No es posible ejecutar el programa 'TestProgram'." in captured.out


def test_executable_programa_not_executable(capsys):
    sim = Simulador()
    sim.define("PROGRAMA", ["TestProgram", "JavaScript"])
    sim.executable("TestProgram")
    captured = capsys.readouterr()
    assert "No es posible ejecutar el programa 'TestProgram'." in captured.out


def test_executable_programa_dont_exist(capsys):
    sim = Simulador()
    sim.executable("TestProgram")
    captured = capsys.readouterr()
    assert "Error: El programa de nombre 'TestProgram' no existe." in captured.out


def test_define_existing_programa(capsys):
    sim = Simulador()
    sim.define("PROGRAMA", ["TestProgram", "Python"])
    sim.define("PROGRAMA", ["TestProgram", "Python"])
    assert "Error: El programa de nombre 'TestProgram' ya existe." in capsys.readouterr().out


def test_run_definir_programa(monkeypatch, capsys):
    sim = Simulador()
    inputs = iter(["DEFINIR PROGRAMA TestProgram LOCAL", "SALIR"])
    monkeypatch.setattr('sys.stdin', StringIO('\n'.join(inputs)))
    sim.run()
    captured = capsys.readouterr()
    assert "Se definió el programa 'TestProgram', ejecutable en 'LOCAL'." in captured.out


def test_run_definir_interprete(monkeypatch, capsys):
    sim = Simulador()
    inputs = iter(["DEFINIR INTERPRETE LOCAL Python", "SALIR"])
    monkeypatch.setattr('sys.stdin', StringIO('\n'.join(inputs)))
    sim.run()
    captured = capsys.readouterr()
    assert "Se definió un intérprete para 'Python' escrito en 'LOCAL'." in captured.out


def test_run_definir_traductor(monkeypatch, capsys):
    sim = Simulador()
    inputs = iter(["DEFINIR TRADUCTOR LOCAL C LOCAL", "SALIR"])
    monkeypatch.setattr('sys.stdin', StringIO('\n'.join(inputs)))
    sim.run()
    captured = capsys.readouterr()
    assert "Se definió un traductor de 'C' a 'LOCAL', escrito en 'LOCAL'." in captured.out


def test_run_ejecutable_programa(monkeypatch, capsys):
    sim = Simulador()
    inputs = iter(["DEFINIR PROGRAMA TestProgram LOCAL",
                   "EJECUTABLE TestProgram", "SALIR"])
    monkeypatch.setattr('sys.stdin', StringIO('\n'.join(inputs)))
    sim.run()
    captured = capsys.readouterr()
    assert "Si, es posible ejecutar el programa 'TestProgram'." in captured.out


def test_run_accion_invalida(monkeypatch, capsys):
    sim = Simulador()
    inputs = iter(["INVALIDO", "SALIR"])
    monkeypatch.setattr('sys.stdin', StringIO('\n'.join(inputs)))
    sim.run()
    captured = capsys.readouterr()
    assert "Accion inválida." in captured.out
