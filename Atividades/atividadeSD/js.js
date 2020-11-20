const App = {
  template: '#app-template',
  data: () => ({
    sticky: false,
    value: 0,
    tab: null,
    items: [
      'SO', 'shopping', 'videos', 'images', 'news',
    ],
    sistemas: [
      {
        nome: 'Sistema Operacional em Lote',
        inform: 'Esse tipo de sistema operacional não interage diretamente com o computador. Existe um operador que pega trabalhos semelhantes com os mesmos requisitos e os agrupa em lotes. É responsabilidade do operador classificar os trabalhos com necessidades semelhantes.',
        img: {
          src: 'imagens/lote.jpeg',
          desc: 'Imagem descritiva de um sistema operacional em lote.'
        },
        vantagem: [
          'É muito difícil adivinhar ou saber o tempo necessário para a conclusão de qualquer trabalho. Os processadores dos sistemas em lote sabem quanto tempo o trabalho demoraria quando estivesse na fila.',
          'Vários usuários podem compartilhar os sistemas em lote.',
          'O tempo ocioso do sistema em lote é muito menor.',
          'É fácil gerenciar grandes trabalhos repetidamente em sistemas em lote.'
        ],
        desvantagem: [
          'Os operadores de computador devem ser bem conhecidos com sistemas batch.',
          'Os sistemas em lote são difíceis de depurar.',
          'Às vezes é caro.',
          'Os outros trabalhos terão que esperar por um tempo desconhecido se algum falhar.'
        ]
      },
      {
        nome: 'Sistemas Operacionais de Compartilhamento de Tempo',
        inform: 'Cada tarefa tem algum tempo para ser executada, para que todas as tarefas funcionem sem problemas. Cada usuário obtém tempo de CPU à medida que usa um único sistema. Esses sistemas também são conhecidos como Sistemas Multitarefa. A tarefa pode ser de um único usuário ou de diferentes usuários também. O tempo que cada tarefa chega para ser executada é chamado de quantum. Após o término desse intervalo de tempo, o sistema operacional muda para a próxima tarefa.',
        img: {
          src: 'imagens/tempo.jpeg',
          desc: 'Imagem descritiva de um Sistemas operacionais de compartilhamento de tempo.'
        },
        vantagem: [
          'Cada tarefa tem oportunidades iguais.',
          'Menos chances de duplicação de software.',
          'O tempo ocioso da CPU pode ser reduzido.'
        ],
        desvantagem: [
          'Problema de confiabilidade.',
          'É necessário cuidar da segurança e integridade dos programas e dados do usuário.',
          'Problema de comunicação de dados.'
        ]
      },
      {
        nome: 'Sistema Operacional de Rede',
        inform: 'esses sistemas são executados em um servidor e fornecem a capacidade de gerenciar dados, usuários, grupos, segurança, aplicativos e outras funções de rede. Esse tipo de sistema operacional permite o acesso compartilhado de arquivos, impressoras, segurança, aplicativos e outras funções de rede em uma pequena rede privada. Um aspecto mais importante dos sistemas operacionais de rede é que todos os usuários estão bem cientes da configuração subjacente, de todos os outros usuários na rede, de suas conexões individuais, etc. e é por isso que esses computadores são popularmente conhecidos como sistemas fortemente acoplados.',
        img: {
          src: 'imagens/rede.jpeg',
          desc: 'Imagem descritiva de um Sistema operacional de rede'
        },
        vantagem: [
          'Servidores centralizados altamente estáveis.',
          'As questões de segurança são tratadas por meio de servidores.',
          'Novas tecnologias e atualização de hardware são facilmente integradas ao sistema.',
          'O acesso ao servidor é possível remotamente de diferentes locais e tipos de sistemas.'
        ],
        desvantagem: [
          'Servidores são caros.',
          'O usuário depende da localização central para a maioria das operações.',
          'Manutenção e atualizações são necessárias regularmente.'
        ]
      },
      {
        nome: 'Sistema Operacional em Tempo Real',
        inform: 'esses tipos de sistemas operacionais atendem aos sistemas em tempo real. O intervalo de tempo necessário para processar e responder às entradas é muito pequeno. Esse intervalo de tempo é chamado de tempo de resposta.',
        img: {
          src: 'imagens/tempoReal.jpeg',
          desc: 'Imagem descritiva de um Sistema operacional em tempo real'
        },
        vantagem: [
          'Utilização máxima de dispositivos e sistema, portanto, mais saída de todos os recursos.',
          'o tempo atribuído para mudanças de tarefas nesses sistemas é muito menor. Por exemplo, em sistemas mais antigos, leva cerca de 10 micro segundos para mudar uma tarefa para outra e em sistemas mais recentes leva 3 micro segundos.',
          'Foco na execução de aplicativos e menos importância para aplicativos que estão na fila.',
          'Como os programas são pequenos, o RTOS também pode ser usado em sistemas embarcados, como transporte e outros.',
          'Esses tipos de sistemas são livres de erros.',
          'A alocação de memória é mais bem gerenciada nesse tipo de sistema.'
        ],
        desvantagem: [
          'muito poucas tarefas são executadas ao mesmo tempo e sua concentração é muito menor em poucos aplicativos para evitar erros.',
          'Às vezes, os recursos do sistema não são tão bons e são caros também.',
          'Os algoritmos são muito complexos e difíceis para o designer escrever.',
          'Ele precisa de drivers de dispositivo específicos e sinais de interrupção para responder o mais rápido possível às interrupções.',
          'Não é bom definir a prioridade do thread, pois esses sistemas são muito menos propensos a alternar tarefas.',
        ]
      },
      {
        nome: 'Sistema Operacional Distribuído',
        inform: 'Esse tipo de sistema operacional é um avanço recente no mundo da tecnologia da computação e está sendo amplamente aceito em todo o mundo e, também, em um ritmo acelerado. Vários computadores autônomos interconectados se comunicam usando uma rede de comunicação compartilhada. Os sistemas independentes possuem sua própria unidade de memória e CPU. Estes são chamados de sistemas fracamente acoplados ou sistemas distribuídos. Os processadores desses sistemas diferem em tamanho e função. O principal benefício de trabalhar com esses tipos de sistema operacional é que sempre é possível que um usuário possa acessar os arquivos ou software que não estão realmente presentes em seu sistema, mas em algum outro sistema conectado nessa rede, ou seja, o acesso remoto está habilitado dentro os dispositivos conectados nessa rede.',
        img: {
          src: 'imagens/distribuido.jpeg',
          desc: 'Imagem descritiva de um Sistema operacional distribuído'
        },
        vantagem: [
          'A falha de um não afetará a comunicação da outra rede, pois todos os sistemas são independentes uns dos outros.',
          'O correio eletrônico aumenta a velocidade de troca de dados.',
          'Como os recursos estão sendo compartilhados, a computação é altamente rápida e durável.',
          'A carga no computador host reduz.',
          'Esses sistemas são facilmente escaláveis, pois muitos sistemas podem ser facilmente adicionados à rede.',
          'O atraso no processamento de dados reduz.'
        ],
        desvantagem: [
          'A falha da rede principal irá interromper toda a comunicação.',
          'Para estabelecer sistemas distribuídos a linguagem que é usada ainda não está bem definida.',
          'Esses tipos de sistemas não estão prontamente disponíveis, pois são muito caros. Não só que o software subjacente é altamente complexo e ainda não é bem compreendido.'
        ]
      },
    ]
  })
}

new Vue({
  vuetify: new Vuetify(),
  render: h => h(App)
}).$mount('#app')