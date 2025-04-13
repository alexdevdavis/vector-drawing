from vector_quadratic_mapper import VectorQuadraticMapper
class MathsSandbox:
    def __init__(self):
        pass

    def main(self):
        print("\n\t🧮 Starting maths sandbox...")
        vqm_10 = VectorQuadraticMapper(10)
        print(vqm_10.vectors)


if __name__ == "__main__":
    sandbox = MathsSandbox()
    sandbox.main()
