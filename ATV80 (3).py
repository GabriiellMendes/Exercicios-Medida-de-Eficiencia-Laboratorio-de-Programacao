from datetime import datetime
from pathlib import Path

pasta = Path(__file__).parent
ARQ_VENDAS = pasta / "vendas.txt"
ARQ_LOG = pasta / "log_erros.txt"
LINHA = "=" * 46


class ProdutoInvalidoError(Exception): pass
class ValorInvalidoError(Exception): pass
class QuantidadeInvalidaError(Exception): pass


def registrar_venda(produto, preco, quantidade):
    if not produto.strip():
        raise ProdutoInvalidoError("O nome do produto não pode ser vazio.")

    try:
        preco = float(preco.replace(",", "."))
    except ValueError:
        raise ValorInvalidoError("O preço deve ser um número.")
    if preco <= 0:
        raise ValorInvalidoError("O preço deve ser maior que zero.")

    try:
        quantidade = int(quantidade)
    except ValueError:
        raise QuantidadeInvalidaError("A quantidade deve ser um número inteiro.")
    if quantidade <= 0:
        raise QuantidadeInvalidaError("A quantidade deve ser um inteiro positivo.")

    return {"produto": produto.strip(), "preco": preco, "quantidade": quantidade, "total": preco * quantidade}


def gravar(arquivo, texto):
    try:
        with open(arquivo, "a", encoding="utf-8") as f:
            f.write(texto + "\n")
    except OSError as erro:
        print(f"  Não foi possível gravar em {arquivo.name}: {erro}")


def gerar_relatorio(vendas):
    print(f"\n{LINHA}\n{'RELATÓRIO DE VENDAS':^46}\n{LINHA}")

    if not vendas:
        print("  Você ainda não registrou nenhuma venda.")
        print("  Volte ao menu e escolha a opção 1 para começar.")
        return

    cabecalho = ("Produto", "Qtd", "Preço", "Total")
    linhas = [(v["produto"], str(v["quantidade"]), f"{v['preco']:.2f}", f"{v['total']:.2f}") for v in vendas]
    larguras = [max(len(l[i]) for l in linhas + [cabecalho]) + 3 for i in range(4)]
    larguras[0] += max(0, 46 - sum(larguras))

    def formatar(l):
        return l[0].ljust(larguras[0]) + "".join(l[i].rjust(larguras[i]) for i in (1, 2, 3))

    print(formatar(cabecalho))
    print("-" * sum(larguras))
    for l in linhas:
        print(formatar(l))

    por_produto = {}
    for v in vendas:
        por_produto[v["produto"]] = por_produto.get(v["produto"], 0) + v["quantidade"]

    faturamento = sum(v["total"] for v in vendas)
    mais_vendido = max(por_produto, key=por_produto.get)

    print("-" * sum(larguras))
    print(f"Total de vendas.....: {len(vendas)}")
    print(f"Produto mais vendido: {mais_vendido} ({por_produto[mais_vendido]} un.)")
    print(f"Faturamento total...: R$ {faturamento:.2f}")
    print(f"Ticket médio........: R$ {faturamento / len(vendas):.2f}")


def nova_venda(vendas):
    produto = input("\n  Por favor, informe o nome do produto: ")
    if produto.strip().lower() == "fim":
        return False
    preco = input("  Informe o preço unitário (R$): ")
    quantidade = input("  Informe a quantidade vendida: ")

    while True:
        try:
            venda = registrar_venda(produto, preco, quantidade)
        except (ProdutoInvalidoError, ValorInvalidoError, QuantidadeInvalidaError) as erro:
            print(f"  [ERRO] {erro} Vamos corrigir?")
            gravar(ARQ_LOG, f"{datetime.now():%d/%m/%Y %H:%M:%S} - {type(erro).__name__}: {erro}")

            novo = input("  Digite o valor correto (ou 'cancelar' para desistir): ")
            if novo.strip().lower() == "cancelar":
                print("  Tudo bem, a venda foi cancelada. Nada foi gravado.")
                break
            if isinstance(erro, ProdutoInvalidoError):
                produto = novo
            elif isinstance(erro, ValorInvalidoError):
                preco = novo
            else:
                quantidade = novo
        else:
            vendas.append(venda)
            gravar(ARQ_VENDAS, f"{venda['produto']};{venda['preco']:.2f};{venda['quantidade']};{venda['total']:.2f}")
            print(f"  [OK] Venda registrada com sucesso! Total: R$ {venda['total']:.2f}")
            break
        finally:
            print("  " + "-" * 30)
    return True


vendas = []

print(f"\n{LINHA}\n{'Bem-vindo(a) à LOJA VIRTUAL!':^46}\n{LINHA}")
print("  Para começar, escolha a opção 1 e cadastre uma venda.")

try:
    while True:
        print(f"\n{LINHA}\n{'MENU PRINCIPAL':^46}\n{LINHA}")
        print(f"  [1] Registrar venda   (vendas hoje: {len(vendas)})")
        print("  [2] Ver relatório\n  [3] Encerrar")
        opcao = input("\n  Escolha uma opção: ").strip().lower()

        if opcao == "1":
            if not nova_venda(vendas):
                break
        elif opcao == "2":
            gerar_relatorio(vendas)
        elif opcao in ("3", "fim"):
            break
        else:
            print("  Opção inválida. Por favor, escolha 1, 2 ou 3.")
except (KeyboardInterrupt, EOFError):
    print("\n\n  Encerrando o programa a pedido do usuário...")

if vendas:
    gerar_relatorio(vendas)
print("\n  Obrigado por usar o sistema. Até logo!")
