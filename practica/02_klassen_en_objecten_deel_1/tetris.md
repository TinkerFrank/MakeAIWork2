```mermaid
classDiagram
    class Block{
     -shape: numpy array
     -color: str
     
     +init(shape, color)
     +rotate(degrees)
     +drop(amount)
     }
```