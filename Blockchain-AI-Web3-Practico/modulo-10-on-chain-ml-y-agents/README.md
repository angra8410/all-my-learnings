# Módulo 10: On-Chain ML y Agents

## 🎯 Objetivos del Módulo

Este módulo te enseñará conceptos y prácticas avanzadas de On-Chain ML y Agents en el contexto de Blockchain y Web3.

**Duración estimada**: 3-5 horas

## 📚 Contenido Principal

Ver `actividad-interactiva.md` para ejercicios prácticos accionables con código listo para copiar/pegar.

## 🔧 Ejemplos Prácticos

Todos los ejemplos incluyen:
- Código Solidity cuando aplique
- JavaScript/TypeScript para interacción
- Docker/docker-compose snippets donde sea relevante
- FastAPI examples para módulos de AI
- Tests y validaciones

## 💡 Conceptos Clave

- Concepto 1: Explicación práctica
- Concepto 2: Código ejecutable
- Concepto 3: Ejemplos reales
- Concepto 4: Mejores prácticas

## 🚀 Quick Start

```bash
# Setup básico
npm install
# o pip install para módulos Python/AI

# Ejecutar ejemplos
npm run example
# o python main.py
```

## 📋 Checklist de Aprendizaje

- [ ] Completar ejercicios prácticos
- [ ] Ejecutar todos los ejemplos de código
- [ ] Pasar tests de validación
- [ ] Construir mini-proyecto del módulo

## 🔗 Recursos Adicionales

- Documentación oficial relevante
- Tutoriales complementarios
- Comunidades y soporte

---

**¡Importante!** Este es un curso 90% práctico. Asegúrate de ejecutar cada ejemplo y completar los ejercicios hands-on.

**Siguiente**: Módulo 11

## 🤖 Trading Agent (Simple)

```python
from web3 import Web3
import time

class SimpleTradingAgent:
    def __init__(self, web3_provider, contract_address, private_key):
        self.w3 = Web3(Web3.HTTPProvider(web3_provider))
        self.contract_address = contract_address
        self.account = self.w3.eth.account.from_key(private_key)
        
    def get_price(self):
        # Mock: en producción consultar oracle real
        return 2000 + (time.time() % 100)
    
    def should_buy(self, price):
        # Estrategia simple: comprar si precio < threshold
        return price < 2050
    
    def should_sell(self, price):
        return price > 2100
    
    def execute_trade(self, action, amount):
        # Construir y enviar transacción
        nonce = self.w3.eth.get_transaction_count(self.account.address)
        
        # Mock transaction (en producción usar contrato real)
        tx = {
            'nonce': nonce,
            'to': self.contract_address,
            'value': amount if action == 'buy' else 0,
            'gas': 200000,
            'gasPrice': self.w3.eth.gas_price
        }
        
        signed = self.w3.eth.account.sign_transaction(tx, self.account.key)
        tx_hash = self.w3.eth.send_raw_transaction(signed.rawTransaction)
        return tx_hash.hex()
    
    def run(self):
        print("🤖 Trading Agent started...")
        while True:
            price = self.get_price()
            print(f"Current price: ${price}")
            
            if self.should_buy(price):
                print("📈 BUY signal")
                # tx_hash = self.execute_trade('buy', Web3.to_wei(0.1, 'ether'))
            elif self.should_sell(price):
                print("📉 SELL signal")
                # tx_hash = self.execute_trade('sell', 0)
            
            time.sleep(10)  # Check every 10 seconds

# Uso
agent = SimpleTradingAgent(
    'http://localhost:8545',
    '0x...',
    'PRIVATE_KEY'
)
# agent.run()
```

## 🎯 Multi-Agent System

```solidity
// Coordinator contract para múltiples agentes
contract AgentCoordinator {
    struct Agent {
        address agentAddress;
        string agentType;
        bool active;
        uint256 successCount;
    }
    
    mapping(address => Agent) public agents;
    address[] public agentList;
    
    event AgentRegistered(address indexed agent, string agentType);
    event TaskAssigned(address indexed agent, bytes32 taskId);
    event TaskCompleted(address indexed agent, bytes32 taskId);
    
    function registerAgent(string memory agentType) external {
        require(!agents[msg.sender].active, "Already registered");
        
        agents[msg.sender] = Agent({
            agentAddress: msg.sender,
            agentType: agentType,
            active: true,
            successCount: 0
        });
        
        agentList.push(msg.sender);
        emit AgentRegistered(msg.sender, agentType);
    }
    
    function reportSuccess(bytes32 taskId) external {
        require(agents[msg.sender].active, "Not registered");
        agents[msg.sender].successCount++;
        emit TaskCompleted(msg.sender, taskId);
    }
    
    function getBestAgent(string memory agentType) public view returns (address) {
        address best;
        uint256 maxSuccess = 0;
        
        for (uint i = 0; i < agentList.length; i++) {
            Agent memory agent = agents[agentList[i]];
            if (agent.active && 
                keccak256(bytes(agent.agentType)) == keccak256(bytes(agentType)) &&
                agent.successCount > maxSuccess) {
                best = agentList[i];
                maxSuccess = agent.successCount;
            }
        }
        
        return best;
    }
}
```
