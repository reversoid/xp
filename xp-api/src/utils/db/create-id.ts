import { init } from "@paralleldrive/cuid2";

export class IdGenerator {
  generateId: () => string;

  constructor(fingerprint: string) {
    this.generateId = init({ length: 10, fingerprint });
  }
}
