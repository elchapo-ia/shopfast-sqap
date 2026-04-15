# ShopFast — Mini SQAP (Software Quality Assurance Plan)

# Política de Quality Gate (baseada na IEEE 730)

Com base nos princípios da IEEE 730, esta política define regras obrigatórias de controle de qualidade que atuam diretamente no pipeline de integração contínua, impedindo que código com falhas críticas chegue ao ambiente de produção.

# Regra 1 — Validação obrigatória de transações

Nenhuma funcionalidade relacionada a pagamento ou aplicação de cupom pode ser integrada ao branch principal sem a validação completa do fluxo de compra.

Isso inclui:

* Aplicação correta do cupom
* Verificação de saldo ou autorização de pagamento
* Confirmação da transação antes da finalização do pedido

Mecanismo de bloqueio:
O pipeline de CI/CD deve impedir o merge caso:

* Algum teste automatizado falhe
* A cobertura de testes na camada de domínio seja inferior a 90%
* Não exista teste validando o fluxo de pagamento


# Regra 2 — Isolamento de regras de negócio

Regras críticas, como cálculo de desconto e validação de pagamento, não podem ser implementadas na camada de interface ou controle.

Essas regras devem estar isoladas na camada de domínio, garantindo previsibilidade, testabilidade e independência de tecnologias externas.

Mecanismo de bloqueio:

* Ferramentas de análise estática devem identificar violações de arquitetura
* O build deve ser interrompido caso haja lógica de negócio na camada de apresentação
* É proibido acesso direto a serviços externos a partir da interface


# Gestão de Risco — Matriz Probabilidade x Impacto

O incidente ocorrido durante a Black Friday é classificado como um risco de alta probabilidade e impacto crítico. A ausência de validação entre aplicação de cupom e confirmação de pagamento permitiu que pedidos fossem processados sem garantia de pagamento, resultando em prejuízo financeiro direto e falha grave de adequação funcional.

A política de qualidade definida atua diretamente na origem do problema ao estabelecer bloqueios automatizados no processo de entrega. Ao exigir validação completa das regras de negócio e impedir acoplamento indevido entre camadas, o sistema passa a rejeitar alterações inconsistentes antes mesmo de chegarem à produção. Como consequência, há uma redução significativa na taxa de falhas em mudanças (Change Failure Rate), garantindo maior estabilidade operacional.


# Regra de Negócio Implementada

O código presente na pasta /src representa a lógica de aplicação de cupom vinculada à validação de saldo. A implementação segue princípios de Clean Code, com separação clara de responsabilidades, uso de exceções específicas e fluxo de execução explícito.

O objetivo é garantir que nenhuma transação seja concluída sem a devida validação financeira, eliminando o risco observado no incidente anterior.


# Conclusão

O problema ocorrido não foi causado por limitação técnica, mas por ausência de controle de qualidade no processo de desenvolvimento.

A adoção de um modelo de SQA com regras claras e mecanismos automáticos de bloqueio garante que erros desse tipo não voltem a ocorrer. O foco deixa de ser a correção após a falha e passa a ser a prevenção, com validações aplicadas diretamente no ciclo de desenvolvimento.
