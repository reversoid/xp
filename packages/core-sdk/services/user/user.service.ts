import { User } from "../../models/user.js";
import { UserRepository } from "../../repositories/user/user.repository.js";
import { CreateUserDto } from "./types.js";

export class UserService {
  private readonly userRepository: UserRepository;

  constructor({ userRepository }: { userRepository: UserRepository }) {
    this.userRepository = userRepository;
  }

  async getUserByTgId(tgId: bigint): Promise<User | null> {
    return this.userRepository.getUserByTgId(tgId);
  }

  async createUser(dto: CreateUserDto) {
    return this.userRepository.createUser({
      tgId: dto.tgId,
      tgUsername: dto.tgUsername,
    });
  }
}
